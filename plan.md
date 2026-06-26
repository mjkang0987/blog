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

## 작업 G: 출처 새창 열기 + 태그/카테고리 필터 (진행 중)

### 요구사항
- 글 하단 **출처 링크를 새 창(새 탭)에서 열기**로 일괄 변경 (기존·향후 글 모두)
- **해시태그 + 카테고리 필터화**: 누르면 해당 항목이 포함된 글 목록을 보여줌
- 필터 방식: **전용 필터 페이지**(`/tags/`) — 실제 URL 링크 기반(웹표준·접근성·SEO 유리)
- UI는 웹표준 + 웹접근성(WCAG) 준수: 시맨틱 HTML, class/id 선택자만, 네이티브 링크 사용

### 구현 방식
- **출처 새창**: `default.html` 하단 JS로 `.post-content` 내 외부 링크(다른 호스트)에만
  `target="_blank"` + `rel="noopener noreferrer"` 부여. 접근성 위해 시각적 숨김 텍스트
  "(새 창에서 열림)"(언어별) 추가 + 외부 링크 아이콘(↗) CSS. 내부 링크(태그 필터)는 제외.
- **필터 페이지**: `tags.html`(permalink `/tags/`, polyglot가 언어별 출력).
  - `site.posts`(언어별)로 태그·카테고리 고유 목록 + 개수 산출(Liquid).
  - 칩(chip)을 `<a href="/tags/?tag=...">`/`?cat=...` 실제 링크로 렌더.
  - 전체 글 카드를 `data-tags`/`data-cats` 속성과 함께 렌더 → JS가 쿼리파라미터로 필터링.
  - JS 없이도 전체 글 표시(graceful degradation). `aria-live`로 결과 수 안내, 활성 칩 `aria-current`.
- **글에서 링크 연결**: `post.html` 푸터 태그를 필터 링크로, 메타 카테고리를 필터 링크로.
  (홈 카드 카테고리는 카드 전체가 링크라 중첩 `<a>` 방지 위해 텍스트 유지)
- 헤더 네비에 "태그"(언어별: 태그/Tags/タグ) 링크 추가로 접근성·발견성 확보.
- CSS: `.filter-page`, `.chip-list`, `.chip`, `.filter-status`, `.visually-hidden`,
  `.external-link` 추가. 태그/카테고리 라벨을 링크로 바꾸며 hover/포커스 가시성 유지.

### 영향받는 파일
- `_layouts/default.html`(외부링크 JS + 네비 링크), `_layouts/post.html`(태그·카테고리 링크화)
- `tags.html`(신규 필터 페이지), `assets/css/main.css`(필터/칩/접근성 스타일)

### 기대 결과
- 출처 링크 클릭 시 새 탭으로 열리고 스크린리더에 새 창 안내됨
- 글의 해시태그/카테고리 클릭 → `/tags/?tag=` 또는 `?cat=`로 이동, 해당 글만 필터링
- JS 비활성 시에도 전체 글·칩 링크 동작(웹표준·접근성 준수)

### 검증
- 로컬 빌드(가능 시) 또는 HTML 구조 점검: 중첩 `<a>` 없음, 시맨틱·aria 속성 확인
- 3개 언어(ko/en-US/ja) 필터 페이지 생성 및 언어별 태그 표시 확인

## 작업 H: 파비콘·로고 (완료)
- 전기 "지지직" 컨셉: 검정 라운드 배경 + 노란(#FFD60A) 번개 + 양옆 크랙클 스파크
- `assets/favicon.svg`(마스터) + `favicon-32.png`/`favicon-256.png`/`apple-touch-icon.png`(불투명)
- `default.html` head에 아이콘 링크 연결, 헤더 `site-brand` 앞에 번개 마크 인라인(aria-hidden 장식)
- 실험용 잡파일(_bolt_*, _logo_candidates 등)은 커밋 제외

## 작업 I: SEO/GEO 강화 (완료)
### 구조화 데이터 + 사이트 메타
- `post.html`에 글별 JSON-LD 추가: **BlogPosting**(headline·description·image·datePublished·dateModified·inLanguage·author·publisher+logo·keywords) + **BreadcrumbList**
- `_config.yml`에 `author`·`logo`(/assets/logo.png)·`social`·`twitter(card: summary_large_image)` 추가 → jekyll-seo-tag JSON-LD/트위터 카드 보강
- 기존 글 9개(_posts ko/en/ja)에 `description`을 `summary`와 동일하게 매핑(검색 메타 설명·JSON-LD용). 향후 글은 스케줄러가 summary+description 동시 출력
### GEO(AI 답변엔진 인용) 최적화
- 자동 발행 프롬프트에 규칙 추가: **answer-first 도입**(첫 1~2문장 80단어 내 핵심 결론), **TL;DR 요약**, **질문형 명확한 소제목 + 섹션 첫 문장 요약**, **구체 수치·날짜·출처 강화**
- `llms.txt`(루트) 추가: 사이트 개요·핵심 링크·언어별 진입점·인용 안내. `exclude_from_localization`에 등록(루트 1회 출력)
- `robots.txt`에 주요 AI/LLM 크롤러(GPTBot·OAI-SearchBot·PerplexityBot·Google-Extended·ClaudeBot·CCBot 등) 허용 명시
### 기존 강점(유지)
- jekyll-seo-tag, sitemap.xml, hreflang(ko/en/ja+x-default), 글별 OG 이미지, 정적 사이트(SSR), 시맨틱 HTML

## 발행 로그
- 2026-06-22 [경제] 원/달러 1,500원대 고환율·외국인 순매도 점검 (ko/en/ja)
- 2026-06-22 [부동산] 수도권 전세난·서울 전셋값 1년 내 최고·경기 남부 확산 (ko/en/ja) — 같은 날 2번째 글, 경제글과 카테고리 분리
- 2026-06-23 [경제] 워시 첫 FOMC 매파적 동결·점도표 상향·유가, 코스피 9000 신고가 (ko/en/ja) — 글로벌 매크로 앵글로 직전 환율/전세 글과 주제 분리
- 2026-06-23 [IT] AI 기본법 시행 5개월·계도기간 1년·고영향/생성형/대규모 AI 의무 정리 (ko/en/ja) — 오후 브리핑, 첫 IT 글(카테고리 균형: IT 0→1), 오전 경제 글과 분리
- 2026-06-24 [부동산] 서울 아파트 6월 선별 강세·규제 속 양극화(6월1주 서울+0.25%/수도권+0.14%/지방 보합, 압구정 신고가 94억) (ko/en/ja) — 오전 브리핑, 부동산 균형 회복(1→2), 직전 IT 글과 분리. 누적 경제 2·부동산 2·IT 1
- 2026-06-24 [IT] HBM '완판 슈퍼사이클'·오늘 밤 마이크론 FQ3 실적(가이던스 매출 ~335억$·GM ~81%)·HBM4 한국 경쟁(SK하이닉스 1위·삼성 양산 반격) (ko/en/ja) — 오후 브리핑, IT 균형 회복(1→2), 오전 부동산 글과 분리. 누적 경제 2·부동산 2·IT 2
- 2026-06-25 [경제] 6월 소비자동향조사 — 소비자심리지수 106.6(+0.5p, 두 달째 100 상회), 금리수준전망 126(+12p, 9년6개월 만 최대폭)·주택가격전망 120(+8p, 5개월 만 최고)·기대인플레 1년 2.8% (ko/en/ja) — 오전 브리핑, 직전 IT 글과 분리, 경제 균형(2→3). 누적 경제 3·부동산 2·IT 2
- 2026-06-25 [IT] 챗GPT 점유율 첫 50% 붕괴 — 센서타워 'State of AI 2026': 챗GPT 5월말 46.4%(첫 과반 붕괴, MAU 11억+), 제미나이 27.7%(MAU 6.6억)·클로드 10.3%(MAU 2.45억) 추격, 클로드 실사용자 +452% YoY·美 4.4→14%, 1Q 상위3사 사용시간 90% (ko/en/ja) — 오후 브리핑, 오전 경제 글과 분리. 어제 IT(HBM 반도체)와 소재 겹치지 않게 AI 챗봇 시장 앵글로 차별화, IT 균형(2→3). 누적 경제 3·부동산 2·IT 3
- 2026-06-25 [IT] (이동·취소) 애플 맥·아이패드 가격 인상 글 — 06-25 19:00 슬롯에서 발행했다가 06-26 오전 슬롯으로 이동, 06-25 파일·OG 3종 제거(중복 방지)
- 2026-06-26 [부동산] (교체·제거) 서울 아파트 6월 4주 외곽·전세 앵글 글 — 자동 발행분이었으나 오전 슬롯을 애플 IT 글로 교체하며 _posts·OG 3종 제거
- 2026-06-26 [부동산] (교체·제거) 서울 아파트값 1년 15%↑·소형 평형 양극화 글 — 06-24 부동산(선별강세·양극화)과 메시지 중복으로 사용자 피드백 반영해 제거, 정책 앵글 글로 교체
- 2026-06-26 [부동산] '실거주 중심' 부동산 세제 개편 시동 — 취득·보유·양도세 통합 '총 세 부담' 재설계, 양도세 장특공제 단순보유분 축소·거주혜택 확대(현 보유40%+거주40%=80%), 보유세 종부세 공정시장가액비율 현60%→80% 상향 카드(시행령 사안, 국회 동의 없이 정부 조정 가능), 다주택 양도세 중과 5/10 재적용, 이달 말 세법개정안 밑그림·다음달 발표 전망 (ko/en/ja) — 오후(19:00) 브리핑(가격글 교체분). 집값 상승이 아닌 '정책 메커니즘' 앵글로 6/22 전세·6/24 선별강세 등 가격 중심 부동산 글과 확실히 차별화. 누적 경제 3·부동산 3·IT 4
- 2026-06-26 [IT] 애플 맥·아이패드 가격 전격 인상 — 'AI 메모리 대란'에 맥 15~20%·아이패드 15~25%↑(맥북네오 599→699$·맥북에어 512GB 1099→1299$·맥북프로 1TB 1699→1999$·아이패드에어 599→749$·아이패드프로 999→1199$), 아이폰 동결, 발표 당일 주가 6%↓·시총 약 2,650억$ 증발, D램/낸드 1년새 4배·마이크론 GM 80%+·공급난 2027년 이후 지속 (ko/en/ja) — 오전 브리핑(수동 교체). 06-25 오후 IT 글(챗GPT 점유율)과 소재 차별화(빅테크 신제품 가격·메모리 대란 앵글). 원화 가격표는 한국 언론 교차검증 미흡으로 % 범위·USD 예시 중심 단정, 정확 원화가는 애플코리아 안내. 누적 경제 3·부동산 2·IT 4(이동 반영: seoul 부동산 글 제거로 부동산 3→2, 애플 IT 유지)
