# My Blog

마크다운으로 글을 발행하는 [Jekyll](https://jekyllrb.com/) 기반 블로그입니다. GitHub Pages 에서 자동으로 빌드/배포됩니다.

## 새 글 발행하기

1. `_posts/` 폴더에 `YYYY-MM-DD-제목.md` 형식으로 파일을 만듭니다.
2. 파일 맨 위에 머리말(front matter)을 작성합니다.

   ```yaml
   ---
   layout: post
   title: "글 제목"
   date: 2026-06-19 09:00:00 +0900
   categories: [카테고리]
   tags: [태그1, 태그2]
   ---
   ```

3. 그 아래에 마크다운으로 본문을 작성합니다.
4. **(한글판) 발행 전 윤문 도구를 돌립니다.** 번역투·이중피동을 교정하고 어미 모노톤·장문을 리포트합니다.

   ```bash
   # 점검만(번역투 발견 시 종료코드 1)
   python3 scripts/humanize_ko.py --check _posts/YYYY-MM-DD-제목.md
   # 교정 적용(파일 덮어씀)
   python3 scripts/humanize_ko.py --fix _posts/YYYY-MM-DD-제목.md
   ```

   - 머리말(front matter)·코드블록·링크 URL은 자동으로 보호됩니다.
   - 어미 모노톤(동일 종결어미 5회+ 연속)·120자 초과 장문은 자동 교정하지 않고 ⚠ 경고만 합니다(문법 손상 방지). 경고가 뜨면 손으로 어미를 변주해 주세요.

5. 커밋 후 푸시하면 GitHub Pages 가 자동으로 발행합니다.

## GitHub Pages 배포 설정 (최초 1회)

1. GitHub 저장소 → **Settings → Pages** 로 이동
2. **Source** 를 `Deploy from a branch` 로 선택
3. **Branch** 를 `main`(또는 발행할 브랜치), 폴더는 `/ (root)` 로 지정 후 저장
4. 잠시 후 `https://<사용자명>.github.io/<저장소명>/` 에서 확인

> 사용자/조직 페이지(`<사용자명>.github.io` 저장소)가 아니라 프로젝트 저장소라면,
> `_config.yml` 의 `baseurl` 을 `"/<저장소명>"` 으로 설정하세요.

## 로컬에서 미리보기 (선택)

```bash
bundle install
bundle exec jekyll serve
# http://localhost:4000 접속
```
