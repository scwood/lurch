module Seize 

  def self.watch(channel, quality)
    exec("livestreamer https://twitch.tv/#{channel} #{quality}")
  end
end
