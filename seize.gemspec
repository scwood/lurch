require File.expand_path("../lib/seize/version", __FILE__)

Gem::Specification.new do |s|
  s.name = 'seize'
  s.version = Seize::VERSION
  s.licenses = ['MIT']
  s.authors = ['Spencer Wood']
  s.email = ['spencercwood@gmail.com']

  s.summary = 'A CLI for Twitch.tv'
  s.description = 'A CLI for Twitch.tv. Full documentation: ' \
                  'https://github.com/scwood/seize'
  s.homepage = 'https://github.com/scwood/seize'

  s.files = Dir.glob('{bin,lib}/**/*') + ['README.md']
  s.bindir = 'bin'
  s.executables  = ['seize']
  s.require_paths = ['lib']

  s.add_dependency('docopt', '0.5.0')
  s.add_dependency('rest-client', '2.0.0')
end
