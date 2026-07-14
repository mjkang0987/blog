#!/usr/bin/env python3
"""
lint_structure.py — 글 구조(섹션 제목/총평/출처) 검증기 · pikaworks blog

발행 파이프라인의 '구조 게이트'. humanize_ko.py 가 산문(번역투·피동)만
검사하는 것과 달리, 이 스크립트는 마크다운 '구조'가 규칙을 지키는지 본다.
섹션 소제목에 '## ' 가 빠져 본문과 같은 크기로 렌더되던 반복 문제를 발행 전에 차단한다.

검사 항목:
  [ERROR] no-heading    : 본문에 섹션 헤딩(##~######)이 하나도 없음 → 소제목이
                          본문 크기로 렌더되는 반복 버그. 발행 차단(종료코드 1).
  [ERROR] dup-title     : 머리말 title 과 (이모지 제외) 동일한 줄이 본문에 중복 등장
  [ERROR] plain-section : 이모지로 시작하고 ' — ' 를 포함하는 섹션 제목이 '## ' 없이 평문
  [WARN ] plain-label   : 총평/출처/TL;DR 라벨이 '## '/볼드 없이 평문(경미·게이트 통과)

ERROR 가 하나라도 있으면 종료코드 1(파이프라인 게이팅용). WARN 만 있으면 0.
--strict 를 주면 WARN 도 종료코드 1 로 취급.

보호 대상: YAML 머리말, 코드펜스(``` ... ```), 목록/인용/표/이미지 줄.

사용:
  python3 scripts/lint_structure.py _posts/2026-07-14-*.md   # 지정 파일
  python3 scripts/lint_structure.py --all                     # _posts 전체
  python3 scripts/lint_structure.py --all --quiet             # 위반 파일만
"""
import argparse
import glob
import os
import re
import sys

# 선두 이모지(변형 선택자 포함) 판별용 대략 범위
EMOJI = re.compile(
    r"^[\U0001F000-\U0001FAFF☀-➿←-⇿⬀-⯿]"
    r"[️‍\U0001F000-\U0001FAFF]*\s"
)
# 라벨형 소제목(언어별 총평/출처/요약)
LABELS = {
    "총평", "출처", "핵심 요약(TL;DR)", "핵심요약(TL;DR)",
    "Overall", "In Sum", "Sources", "TL;DR",
    "総評", "出典", "要点(TL;DR)",
}
BOLD_LABEL = re.compile(r"^\*\*.+\*\*$")
# 문장(마침표/물음표로 끝나는 긴 줄)은 제목이 아님
SENTENCE_END = ("다.", "요.", ".", "?", "!", "。")


def strip_lead_emoji(s):
    m = EMOJI.match(s)
    return s[m.end():].strip() if m else s.strip()


def split_front_matter(text):
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[: i + 1], lines[i + 1:]
    return [], lines


def get_title(front):
    for ln in front:
        m = re.match(r'^title:\s*"?(.*?)"?\s*$', ln)
        if m:
            return strip_lead_emoji(m.group(1))
    return None


def classify_plain(line):
    """평문인데 제목처럼 보이는가? 'section'(ERROR)/'label'(WARN)/None 반환."""
    s = line.strip()
    if not s or s.startswith(("-", "*", ">", "|", "!", "#", "[")):
        return None
    if BOLD_LABEL.match(s):
        return None
    # 이모지 선두 + em-dash(≈ 섹션 제목) — 문장부호로 끝나지 않을 때
    if EMOJI.match(s) and (" — " in s or " – " in s) and not s.endswith(SENTENCE_END):
        # 라벨(총평/Overall/総評)을 이모지로 감싼 경우도 섹션 취급
        return "section"
    # 라벨형(총평/출처/TL;DR) — 이모지 유무와 무관하게 경미
    if strip_lead_emoji(s) in LABELS:
        return "label"
    return None


def lint(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    front, body = split_front_matter(text)
    title = get_title(front)

    errors = []
    in_code = False
    heading_count = 0
    for i, line in enumerate(body):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        # ATX 헤딩(##~######) 모두 헤딩으로 집계 — h3(###)도 실제 소제목임
        if re.match(r"^#{2,6} ", s):
            heading_count += 1
            continue
        kind = classify_plain(line)
        if kind == "section":
            errors.append(("ERROR", i + 1, "plain-section", s[:60]))
        elif kind == "label":
            errors.append(("WARN", i + 1, "plain-label", s[:60]))
        if title and strip_lead_emoji(s) == title and len(title) > 12:
            errors.append(("ERROR", i + 1, "dup-title", s[:60]))

    if heading_count == 0:
        errors.insert(0, ("ERROR", 0, "no-heading", "본문에 섹션 헤딩(##~######)이 없음"))
    return errors, heading_count


def main():
    ap = argparse.ArgumentParser(description="글 구조(섹션 제목) 검증기")
    ap.add_argument("files", nargs="*", help="대상 .md 파일")
    ap.add_argument("--all", action="store_true", help="_posts 전체 검사")
    ap.add_argument("--quiet", action="store_true", help="위반 파일만 출력")
    ap.add_argument("--strict", action="store_true", help="WARN 도 실패로 취급")
    args = ap.parse_args()

    files = args.files
    if args.all:
        base = os.path.join(os.path.dirname(__file__), "..", "_posts")
        files = sorted(glob.glob(os.path.join(base, "*.md")))
    if not files:
        ap.error("검사할 파일을 지정하거나 --all 을 사용하세요.")

    err_files = warn_files = 0
    for path in files:
        errors, hc = lint(path)
        name = os.path.basename(path)
        has_err = any(sev == "ERROR" for sev, *_ in errors)
        has_warn = any(sev == "WARN" for sev, *_ in errors)
        if has_err:
            err_files += 1
        elif has_warn:
            warn_files += 1
        if errors:
            mark = "✗" if has_err else "△"
            print(f"\n{mark} {name}  (헤딩 {hc}개)")
            for sev, ln, code, msg in errors:
                loc = f"L{ln}" if ln else "  "
                print(f"    [{sev:5}] {code} {loc}: {msg}")
        elif not args.quiet:
            print(f"✓ {name}  (헤딩 {hc}개)")

    print(f"\n검사 {len(files)}건 · ERROR {err_files}건 · WARN {warn_files}건")
    fail = err_files or (args.strict and warn_files)
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
