# frozen_string_literal: true

# jekyll-seo-tag 가 출력하는 og:url 은 항상 기본언어(ko) 경로를 가리킨다.
# polyglot 은 출력 HTML 에서 href="..." 속성만 언어 프리픽스로 다시 쓰고
# <meta content="..."> 는 손대지 않으므로, 번역 페이지의 og:url 이 ko 주소로 남는다.
# (canonical 은 href 라서 polyglot 이 이미 올바르게 보정함)
#
# 이 훅은 비(非)기본언어 문서의 og:url content 에만 언어 프리픽스를 넣어 보정한다.
# polyglot 이 절대 건드리지 않는 content= 만 수정하므로 실행 순서와 무관하게 안전하다.
Jekyll::Hooks.register %i[documents pages], :post_render do |item|
  site = item.site
  default_lang = site.config['default_lang'] || (site.config['languages'] || []).first
  # 현재 출력 중인 언어. 홈/소개 등은 front matter lang(ko)이 고정돼 있어도
  # polyglot 이 /en-US/·/ja/ 로 함께 출력하므로, 빌드 언어(active_lang)를 기준으로 삼는다.
  lang = (site.respond_to?(:active_lang) && site.active_lang) || item.data['lang']
  next if lang.nil? || lang.to_s.empty? || lang == default_lang

  base_url = site.config['url'].to_s
  next if base_url.empty? || item.output.nil?

  # <meta property="og:url" content="https://host/<경로>"> 의 도메인 직후에
  # 이미 /<lang>/ 가 없을 때만 프리픽스를 삽입한다.
  pattern = /(<meta property="og:url" content="#{Regexp.escape(base_url)})\/(?!#{Regexp.escape(lang)}\/)/
  item.output = item.output.sub(pattern, "\\1/#{lang}/")
end
