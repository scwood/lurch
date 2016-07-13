require 'seize/version'

Gem::Specification.new do |s|
  s.name = 'seize'
  s.version = Seize::VERSION
  s.authors = ['Spencer Wood']
  s.email = ['spencercwood@gmail.com']

  s.summary = 'Twitch.tv CLI interface'
  s.description = 'Full documentation: https://github.com/scwood/seize'
  s.homepage = 'https://github.com/scwood/seize'

  s.files = Dir.glob("{bin,lib}/**/*") + ['README.md']
  s.bindir = "bin"
  s.executables  = ['seize']
  s.require_paths = ['lib']

  s.add_dependency("docopt")
  s.add_dependency("rest-client")
end
