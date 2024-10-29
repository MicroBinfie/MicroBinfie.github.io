source "https://rubygems.org"
# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!
gem "jekyll", "~> 3.10.0"
#gem "jekyll"
# This is the default theme for new Jekyll sites. You may change this to anything you like.
gem "minima", "~> 2.5"
gem "jekyll-theme-minimal"
gem "jekyll-theme-tactile"
#gem "jekyll-sound_cloud"
gem "kramdown-parser-gfm"
gem "jekyll-embeds"
gem 'jekyll_picture_tag'

# jekyll-text-theme and deps
#gem "jekyll-text-theme"
group :development do
  gem 'appraisal'
  gem 'bundler'
  gem 'rake'
end
# jekyll-text-theme and deps
group :test do
  gem 'commonmarker', '~> 0.23', require: false
  gem 'email_reply_parser', '~> 0.5', require: false
  gem 'gemoji', '~> 3.0', require: false
  gem 'minitest'
  gem 'RedCloth',           '~> 4.3.0', require: false
  gem 'rinku',              '~> 1.7',   require: false
  gem 'sanitize',           '~> 6.0.1', require: false

  gem 'escape_utils', '~> 1.0', require: false
  gem 'rouge', '~> 3.30', require: false
  gem 'minitest-focus', '~> 1.1'
end

#gem "github-pages", group: :jekyll_plugins
# If you want to use GitHub Pages, remove the "gem "jekyll"" above and
# uncomment the line below. To upgrade, run `bundle update github-pages`.
# gem "github-pages", group: :jekyll_plugins
# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.17"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

