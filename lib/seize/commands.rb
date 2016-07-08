module Seize 

  def self.watch(channel, quality)
    exec("livestreamer https://twitch.tv/#{channel} #{quality}")
  end

  def self.list(number)

  end
end
