# frozen_string_literal: true

require 'yaml'

# 글별로 실제 존재하는 언어판 목록을 site.data['post_langs'] = { permalink => [lang, ...] } 로 만든다.
# polyglot 은 번역이 없는 ko 글도 /en-US/·/ja/ 경로에 한국어 그대로 출력(폴백)하므로,
# 레이아웃·사이트맵이 이 목록으로 "진짜 번역판"만 hreflang·sitemap 에 싣고 폴백 페이지는 noindex 한다.
# 언어별 빌드마다 site.posts 가 걸러지므로 디스크의 _posts 를 직접 읽는다.
Jekyll::Hooks.register :site, :post_read do |site|
  default_lang = site.config['default_lang'] || 'ko'
  index = Hash.new { |h, k| h[k] = [] }
  Dir.glob(File.join(site.source, '_posts', '*.md')).sort.each do |path|
    front = File.read(path, encoding: 'utf-8')[/\A---\s*\n(.*?)\n---/m, 1]
    next unless front

    data = YAML.safe_load(front, permitted_classes: [Date, Time]) || {}
    permalink = data['permalink']
    next unless permalink

    lang = data['lang'] || default_lang
    index[permalink] << lang unless index[permalink].include?(lang)
  end
  # 언어 순서는 _config.yml languages 순서로 고정
  order = site.config['languages'] || [default_lang]
  site.data['post_langs'] = index.transform_values { |langs| langs.sort_by { |l| order.index(l) || order.size } }
end
