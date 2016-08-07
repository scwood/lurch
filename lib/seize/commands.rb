require 'json'

require 'seize/twitch'
require 'seize/utils'

module Seize 
  def self.watch(channel, quality)
    exec("livestreamer https://twitch.tv/#{channel} #{quality}")
  end

  def self.list(number)
    line_length = 79
    number_length = 5
    name_length = 20
    viewers_length = 12
    game_length = 40
    row_template = " %-#{number_length}{number}" \
                   " %-#{name_length}{name}" \
                   " %-#{viewers_length}{viewers}" \
                   " %{game}\n"
    result = ''
    line = '-' * line_length << "\n"
    result << line
    result << row_template % {
      number: '#',
      name: 'channel',
      viewers: 'viewers',
      game: 'game'
    } 
    result << line
    streams = Seize::Twitch.get_streams(limit: number)['streams']
    streams.each_with_index do |stream, i|
      result << row_template % {
        number: "#{i+1}.",
        name: Seize::Utils.truncate(stream['channel']['name'], name_length),
        viewers: Seize::Utils.commaize(stream['viewers']),
        game: Seize::Utils.truncate(stream['game'], game_length)
      }
    end
    puts result
  end

  def self.check(channel_name)
    channel = Seize::Twitch.get_channel(channel_name)
    if channel.nil?
      puts 'error: channel does not exist'
    elsif channel['stream'].nil?
      puts "#{channel_name} is offline"
    else
      game = channel['stream']['game']
      viewers = Seize::Utils.commaize(channel['stream']['viewers'])
      puts "#{channel_name} is playing #{game} with #{viewers} viewers"
    end
  end
end
