import requests
import subprocess

class Client(object):

    def __init__(self):
        self.base_url = 'https://api.twitch.tv/kraken'

    """Returns a list of online channels.

    Args:
        n: Number of channels to return. The Twitch API will only return a max
        of 100 channels.
    Returns:
        A list of channels sorted by number of viewers
    Raises:
        Connection Error if Twitch.tv cannot be reached.
    """
    def get_online_channels(self, n=25):
        if not self._can_connect_to_twitch():
            raise ConnectionError("Can't connect to Twitch.tv")
        url = self.base_url + '/streams'
        params = {'limit': n}
        response = self._api_get(url, params)
        channels = [{
            'name': stream['channel']['display_name'],
            'viewers': stream['viewers'],
            'game': stream['game'] 
        } for stream in response['streams']]
        return channels

    def get_channel_status(self, channel):
        pass

    def watch_channel(self, channel, quality):
        subprocess.call(['livestreamer', 'http://twitch.tv/'+channel, quality])

    def _can_connect_to_twitch(self):
        try:
            check = requests.get('http://www.twitch.tv/')
        except requests.ConnectionError:
            return False
        return True

    def _api_get(self, url, params=None):
        r = requests.get(url, params=params)
        return r.json()

