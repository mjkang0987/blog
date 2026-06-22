# plan.md

## 진행 중 작업 A: 호스팅 + 다국어(i18n) 구성

### 요구사항
- 커스텀 도메인: **blog.pikaworks.kr** (가비아 CNAME → mjkang0987.github.io, 전파 완료)
- 다국어 3개: 한국어 · 영문 · 일본어
- (1차 배포) 표준 구성: **한국어 루트 `/`, 영문 `/en-US/`, 일문 `/ja/`**
- (TODO) `/ko` 프리픽스 + 루트 리다이렉트는 파이프라인 검증 후 적용 검토
  - 사유: polyglot의 기본언어 서브폴더화는 비공식 우회(루트 패스 충돌 위험)이고, 샌드박스에서 rubygems 차단(403)으로 로컬 빌드 검증 불가
- 빌드: **GitHub Actions** (polyglot는 GitHub Pages 기본 빌드 화이트리스트에 없어 직접 빌드 필요)
- 배포 브랜치: **main** (기존 develop → main 일원화)

### 구현 방식
- 플러그인: `jekyll-polyglot` + `jekyll-feed` + `jekyll-seo-tag`, 테마 `minima`
- `github-pages` gem 제거 → `jekyll`(4.x) 직접 사용 (Actions 빌드라 가능)
- `_config.yml`:
  - `url: https://blog.pikaworks.kr`, `baseurl: ""`
  - `languages: ["ko", "en-US", "ja"]`, `default_lang: "ko"` (안정적 표준 구성)
  - `exclude_from_localization`로 assets·CNAME·sitemap 등 루트 1회 출력
- `.github/workflows/jekyll.yml`: ruby/setup-ruby + bundler 캐시 → `bundle exec jekyll build` → `actions/deploy-pages`
- `CNAME` 파일: `blog.pikaworks.kr`

### 사용자 수동 작업
- GitHub 저장소 Settings → Pages → **Source = GitHub Actions**
- (DNS는 완료됨)

### 영향받는 파일
- `Gemfile`, `_config.yml`, `.github/workflows/jekyll.yml`, `CNAME`, `index.html`
- `about.md`, `_posts/*` → 언어별(`lang`) 구성

### 기대 결과
- `blog.pikaworks.kr/ko`, `/en-US`, `/ja` 정상 표시, 루트는 `/ko` 리다이렉트
- main 푸시 시 Actions가 자동 빌드·배포

### 검증
- Actions 빌드 성공 확인
- 배포된 사이트에서 3개 언어 경로 + 루트 리다이렉트 + HTTPS 확인

---

## 작업 B: 매일 경제/부동산 블로그 자동 발행 (호스팅 완료 후 등록)

### 요구사항
- 매일 밤 21시(KST) 자동 실행 (리마인더 X, 완전 자동 작성)
- 카테고리: 경제 / 부동산
- 글 종류(우선순위 1일 > 일요일 > 평소):
  - 매월 1일: 지난달 회고 + 다음달 전망 (심층)
  - 매주 일요일: 금주 마무리 회고 + 다음주 전망 (심층)
  - 그 외: 그날 이슈 큰 주제(경제 or 부동산) 가변 분량 브리핑
- **뚜렷한 경제/부동산 뉴스 없으면 → 수도권(서울·경기·인천) 지역을 순환하며 한 곳씩, 시세·거래량·입지·전망·호재·악재 정리** (한국부동산원·KB부동산 통계 + 호재/악재 검색, 최근 글과 안 겹치게)
- **주식 관련 내용은 구체적 종목 언급 금지**
- 범위: 한국 + 글로벌
- 말투: **정중한 문어체(~입니다/~합니다)**, 친절하고 구체적으로 설명 — 글로벌 음슴체 설정을 이 작업에서만 오버라이드
- CTR 제목, 이모지, 해시태그 10-15개, 서술형 금지
- 투자 추천 금지 — 사실·데이터 위주 + "투자 조언 아님" 단서 + 출처 표기
- **3개 언어(ko/en-US/ja) 동시 발행**
- 발행 방식: 선발행 후공유 (자동 커밋·푸시 후 사용자에게 글 공유)

### 구현 방식
- 스케줄 작업(`daily-blog-post`) cron `0 21 * * *` (KST 로컬), 날짜 보고 글 종류 분기
- 글 파일: 언어별 `_posts/`에 `lang` 지정, 동일 `page_id`/permalink로 연결
- 출처는 글 하단에 표기

### 기대 결과
- 매일 21시 경제/부동산 글이 3개 언어로 자동 작성·발행되고 사용자에게 공유됨

## 작업 C: 커스텀 UI (완료)
- minima 테마 제거 → 커스텀 레이아웃(default/home/post/page) + `assets/css/main.css`
- 디자인: 깔끔·미니멀, 브랜드 `#6526d9`, 대비(헤더·푸터) `#1c1c1e`
- 헤더에 언어 스위처(한국어/EN/日本語, polyglot `static_href`) + 주 메뉴(홈/소개) 다국어
- 프론트 규칙 준수: 시맨틱 HTML, 클래스/ID 선택자(마크다운 본문만 `.post-content` 하위 스코프), 스킵 링크·포커스 가시성(WCAG)

## 작업 D: 추가 콘텐츠 자동화 (도구화됨)
- humanize-korean 플러그인 설치 → 매일 작업의 한글판 발행 전 윤문 단계로 연결

## 작업 F: UI 개선 (진행 중)
- 언어 스위처를 네이티브 `<select>` 박스로 변경(🌐 + 한국어/English/日本語)
- 홈 글 목록을 OG 썸네일 카드 그리드로(2열, 모바일 1열)
- 카드 하단에 한 줄 요약(`summary` front matter, 없으면 excerpt 폴백) 추가
- CSS 링크에 빌드 버전 쿼리 → 브라우저 캐시 무력화
- 카드 썸네일 `height:auto`로 종횡비 정상화

## 작업 E: SEO + OG 이미지 (완료)
- jekyll-seo-tag(title·description·OG·트위터·canonical) + jekyll-feed 기존 적용
- **hreflang** 태그(ko/en-US/ja + x-default) `default.html` head에 추가(동일 permalink 프리픽스 방식, polyglot static_href)
- **jekyll-sitemap**(`/sitemap.xml`) + **robots.txt** 추가
- **OG 이미지 자동 생성**: `scripts/og_image.py`(PIL+Noto CJK) — 1200×630 브랜드 카드(제목+카테고리+사이트명), 이모지 자동 제거. 글마다 `image:` front matter 연결 → og:image/twitter summary_large_image
- 매일 자동화에 OG 이미지 생성 단계 포함(언어별 -ko/-en/-ja)

## 향후 작업(Backlog)
- 다국어 sitemap 정밀화(현재 기본언어 중심 + hreflang 보완)
- 카테고리별 글 템플릿 정교화
- 첫 1~2주 글 품질 모니터링 후 프롬프트 조정
- humanize 룰북 정밀 적용(플러그인 폴더 연결 검토)
- 기본 OG 이미지/대표 이미지 디자인 고도화

## 발행 로그
- 2026-06-22 [경제] 원/달러 1,500원대 고환율·외국인 순매도 점검 (ko/en/ja)
- 2026-06-22 [부동산] 수도권 전세난·서울 전셋값 1년 내 최고·경기 남부 확산 (ko/en/ja) — 같은 날 2번째 글, 경제글과 카테고리 분리
