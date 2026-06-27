#!/usr/bin/env python3
"""
humanize_ko.py — 한글 글 윤문(번역투/이중피동/군더더기) 교정기 · pikaworks blog

plan.md 작업 D("한글판 발행 전 윤문 단계")의 실제 구현체입니다.
네트워크/LLM 의존 없이 규칙 기반으로 동작하므로, 스케줄 자동 발행 파이프라인에서
안전하게 호출할 수 있습니다.

보호 대상(교정에서 제외):
  - YAML 머리말(front matter, 맨 앞 --- ... ---)
  - 코드펜스(``` ... ```)와 인라인 코드(`...`)
  - 링크 URL 부분 ](http...)  ※ 링크 표시 텍스트(한글)는 교정 대상

기능:
  - --fix    : 안전한 치환을 적용해 파일을 덮어씀(또는 --stdout)
  - --check  : 교정 대상/주의 항목만 리포트(기본값). 발견 시 종료코드 1
  - --diff   : 변경 전/후 라인을 함께 출력

사용:
  python3 scripts/humanize_ko.py --check _posts/2026-06-27-*.md
  python3 scripts/humanize_ko.py --fix   _posts/2026-06-27-foo.md
  python3 scripts/humanize_ko.py --fix --diff _posts/foo.md
"""
import argparse
import re
import sys

# ── 1) 안전한 직접 치환(번역투·군더더기) ──────────────────────────────
#   (패턴, 치환, 설명)  순서대로 적용되므로 더 긴 패턴을 먼저 둔다.
REPLACERS = [
    # 번역투 연결어미 '~하여' → '~해'
    ("에 대하여", "에 대해", "번역투(에 대하여)"),
    ("에 관하여", "에 관해", "번역투(에 관하여)"),
    ("으로 인하여", "으로 인해", "번역투(으로 인하여)"),
    ("로 인하여", "로 인해", "번역투(로 인하여)"),
    ("를 통하여", "를 통해", "번역투(를 통하여)"),
    ("을 통하여", "을 통해", "번역투(을 통하여)"),
    ("에 의하여", "에 의해", "번역투(에 의하여)"),
    ("에 있어서", "에서", "번역투(에 있어서)"),
    ("에 있어", "에서", "번역투(에 있어)"),
    # 군더더기/상투 표현
    ("~라고 할 수 있습니다", "입니다", "군더더기(라고 할 수 있습니다)"),
    ("는 것이 사실입니다", "는 게 사실입니다", "딱딱한 문어투(것이→게)"),
]

# ── 2) 이중피동 교정(피동 + 어지다 중복) ─────────────────────────────
#   복합 한글 음절 분해가 까다로워 자주 쓰이는 활용형을 명시적으로 매핑한다.
DOUBLE_PASSIVE = [
    # 보여지다 → 보이다
    ("보여집니다", "보입니다"), ("보여진다", "보인다"), ("보여졌습니다", "보였습니다"),
    ("보여졌다", "보였다"), ("보여지는", "보이는"), ("보여질", "보일"), ("보여진", "보인"),
    # 되어지다 → 되다
    ("되어집니다", "됩니다"), ("되어진다", "된다"), ("되어졌습니다", "됐습니다"),
    ("되어졌다", "됐다"), ("되어지는", "되는"), ("되어질", "될"), ("되어진", "된"),
    # 불려지다 → 불리다
    ("불려집니다", "불립니다"), ("불려진다", "불린다"), ("불려졌습니다", "불렸습니다"),
    ("불려지는", "불리는"), ("불려진", "불린"),
    # 쓰여지다 → 쓰이다
    ("쓰여집니다", "쓰입니다"), ("쓰여진다", "쓰인다"), ("쓰여진", "쓰인"),
    ("쓰여지는", "쓰이는"),
    # 모여지다 → 모이다 / 짜여지다 → 짜이다
    ("모여진", "모인"), ("짜여진", "짜인"),
]

ENDINGS = ("습니다", "입니다", "됩니다", "합니다", "ㅂ니다")
SENT_SPLIT = re.compile(r"(?<=다\.)\s+|(?<=요\.)\s+")


def split_protect(text):
    """본문에서 인라인 코드와 링크 URL을 자리표시자로 보호."""
    saved = []

    def stash(m):
        saved.append(m.group(0))
        return f"\x00{len(saved)-1}\x00"

    # 인라인 코드 `...`
    text = re.sub(r"`[^`]*`", stash, text)
    # 링크 URL 부분 ](...)
    text = re.sub(r"\]\([^)]*\)", stash, text)
    return text, saved


def restore(text, saved):
    for i, s in enumerate(saved):
        text = text.replace(f"\x00{i}\x00", s)
    return text


def humanize_line(line):
    """한 줄 prose 교정. (새 줄, 적용된 설명 리스트) 반환."""
    protected, saved = split_protect(line)
    notes = []
    out = protected
    for pat, rep in DOUBLE_PASSIVE:
        if pat in out:
            out = out.replace(pat, rep)
            notes.append(f"이중피동({pat}→{rep})")
    for pat, rep, desc in REPLACERS:
        if pat in out:
            out = out.replace(pat, rep)
            notes.append(desc)
    # 중복 공백 정리(자리표시자/들여쓰기 보존 위해 라인 중간만)
    collapsed = re.sub(r"(?<=\S)  +(?=\S)", " ", out)
    if collapsed != out:
        notes.append("중복 공백 정리")
        out = collapsed
    return restore(out, saved), notes


def process(text):
    """문서 전체 처리. (새 텍스트, 변경 리스트, 경고 리스트) 반환."""
    lines = text.split("\n")
    in_front = False
    front_done = False
    in_code = False
    changes = []
    new_lines = []
    body_for_warn = []

    for idx, line in enumerate(lines):
        stripped = line.strip()
        # front matter 경계(맨 앞 ---)
        if idx == 0 and stripped == "---":
            in_front = True
            new_lines.append(line)
            continue
        if in_front:
            new_lines.append(line)
            if stripped == "---":
                in_front = False
                front_done = True
            continue
        # 코드펜스 토글
        if stripped.startswith("```"):
            in_code = not in_code
            new_lines.append(line)
            continue
        if in_code:
            new_lines.append(line)
            continue
        # 출처/링크만 있는 줄도 표시 텍스트 교정은 허용하되 URL은 보호됨
        new_line, notes = humanize_line(line)
        if notes:
            changes.append((idx + 1, line, new_line, notes))
        new_lines.append(new_line)
        if stripped and not stripped.startswith(("#", "-", "*", ">", "|", "![")):
            body_for_warn.append(new_line)

    warnings = _warn(" ".join(body_for_warn))
    return "\n".join(new_lines), changes, warnings


def _warn(body):
    """자동 교정하지 않고 리포트만: 어미 모노톤·장문."""
    warns = []
    sents = [s for s in SENT_SPLIT.split(body) if s.strip()]
    # 어미 모노톤: 동일 종결어미 5회 이상 연속
    run, prev, max_run = 0, None, 0
    for s in sents:
        end = next((e for e in ENDINGS if s.rstrip().endswith(e + ".") or s.rstrip().endswith(e)), None)
        if end and end == prev:
            run += 1
            max_run = max(max_run, run)
        else:
            run, prev = 1, end
    if max_run >= 5:
        warns.append(f"동일 종결어미 {max_run}회 연속 — 어미 변주 권장")
    # 장문: 120자 초과 문장 수
    longs = [s for s in sents if len(s.strip()) > 120]
    if longs:
        warns.append(f"120자 초과 장문 {len(longs)}건 — 분할 검토")
    return warns


def main():
    ap = argparse.ArgumentParser(description="한글 글 윤문(번역투/이중피동) 교정기")
    ap.add_argument("files", nargs="+", help="대상 .md 파일")
    ap.add_argument("--check", action="store_true", help="리포트만(기본값)")
    ap.add_argument("--fix", action="store_true", help="교정 적용(파일 덮어씀)")
    ap.add_argument("--stdout", action="store_true", help="--fix 결과를 표준출력으로")
    ap.add_argument("--diff", action="store_true", help="변경 전/후 라인 출력")
    args = ap.parse_args()

    total_changes = 0
    total_warns = 0
    for path in args.files:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        new_text, changes, warnings = process(text)
        total_changes += len(changes)
        total_warns += len(warnings)

        head = f"\n■ {path}"
        if changes or warnings:
            print(head)
        for ln, before, after, notes in changes:
            print(f"  L{ln}: {', '.join(notes)}")
            if args.diff:
                print(f"      - {before.strip()}")
                print(f"      + {after.strip()}")
        for w in warnings:
            print(f"  ⚠ {w}")

        if args.fix and new_text != text:
            if args.stdout:
                sys.stdout.write(new_text)
            else:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_text)
                print(f"  ✔ 적용됨: {len(changes)}건 교정")

    if not args.fix:
        print(f"\n총 교정대상 {total_changes}건 · 경고 {total_warns}건")
        # 교정 대상이 있으면 종료코드 1(파이프라인 게이팅용)
        sys.exit(1 if total_changes else 0)


if __name__ == "__main__":
    main()
