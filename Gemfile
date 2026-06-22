source "https://rubygems.org"

# GitHub Actions 로 직접 빌드 (github-pages gem 미사용 → polyglot 등 자유롭게)
gem "jekyll", "~> 4.3"

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
  gem "jekyll-polyglot"
end

# Ruby 3+ 로컬 서빙용
gem "webrick", "~> 1.8"

# Windows / macOS 호환용
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]
