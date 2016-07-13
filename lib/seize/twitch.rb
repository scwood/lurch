require 'rest-client'

module Seize
  module Twitch
    BASE_URL = 'https://api.twitch.tv/kraken'
    HEADERS = {:accept => 'application/vnd.twitchtv.v3+json',
               :'client-id' => '2n7irufqjtyyayigyc4ubzq174axeex'}

    # TODO support games paramater
    def self.get_streams(limit: nil)
      streams_response = RestClient.get("#{BASE_URL}/streams", {
        :params => { :limit => limit }, :headers => HEADERS,
      })
      JSON.parse(streams_response)
    end

    def self.get_channel(channel_name)
      begin
        channel_response = RestClient.get(
          "#{BASE_URL}/streams/#{channel_name}",
          { :headers => HEADERS })
        JSON.parse(channel_response)
      rescue RestClient::NotFound
        nil
      end
    end
  end
end
