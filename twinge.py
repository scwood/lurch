import click
import json
import os.path
import requests

from subprocess import call

@click.group()
@click.help_option('--help')
def cli():
    '''Twinge is a CLI for Twitch.tv. Twinge can do a number of things
    including browsing the top channels, checking user followed channels,
    or checking the status of a particular channel. It also provides an easy
    shortcut into livestreamer to make launching twitch streams from the command
    line easy.
    '''

@cli.command(short_help='Lists the top live channels.')
@click.help_option('--help')
@click.option('--number', '-n', default=25, required=False,
        type=click.IntRange(1, 100),
        help='Changes the number of channels to list.')
def list(number):
    '''This will list the top channels that are currently live on twitch
    sorted by number of viewers. It will also caches the streams locally so
    '''
    print_list(number)

def print_list(number):
    if not can_connect_to_twitch():
        return
    url = 'https://api.twitch.tv/kraken/streams?limit=' + str(number)
    api_call = requests.get(url)
    twitch_data = api_call.json()
    streams = twitch_data['streams']
    streams_cache = {}
    line_size = 79
    number_size = 5
    name_size = 22
    viewers_size = 11
    game_size = 41
    header = '{0:<%d}{1:<%d}{2:<%d}' % (number_size, name_size, viewers_size)
    content = '{0:<%d}{1:<%d}{2:<%d,}' % (number_size, name_size, viewers_size)
    click.echo('-' * line_size)
    click.echo(header.format(' #', 'channel', 'viewers') + 'game')
    click.echo('-' * line_size)
    for x in range(0, len(streams)):
        number = ' ' + str(x + 1) + '.'
        name = trim(streams[x]['channel']['display_name'], name_size - 1)
        streams_cache[x + 1] = name
        viewers = streams[x]['viewers']
        game = trim(streams[x]['game'], game_size - 1)
        click.echo(content.format(number, name, viewers) + game)
    cache_streams(streams_cache)

def can_connect_to_twitch():
    try:
        check = requests.get('http://www.twitch.tv/')
        return True
    except requests.ConnectionError:
        click.echo('Error: can\'t reach twitch.tv')
    return False

def trim(string, length):
    if string is None:
        return 'None'
    elif len(string) <= length:
        return string
    else:
        return string[0:length - 3] + '...'

def cache_streams(streams):
    with open('streams_cache.json', 'w') as outfile:
        json.dump(streams, outfile, indent = 2)

@cli.command(short_help='Checks the status of a single channel.')
@click.argument('channel')
@click.help_option('--help')
def check(channel):
    '''This will check if a particular channel is currently online or not,
    and if it is will provide additional information.
    '''
    print_check(channel)

def print_check(channel):
    if not can_connect_to_twitch():
        return
    url = 'https://api.twitch.tv/kraken/streams/' + channel
    api_call = requests.get(url)
    twitch_data = api_call.json()
    if 'Error' in twitch_data:
        click.echo('Error: ' + channel + ' is not a valid channel name')
    elif twitch_data['stream'] == None:
        click.echo(channel + ' is offline')
    else:
        name = twitch_data['stream']['channel']['display_name'];
        game = twitch_data['stream']['game']
        viewers = '{:,}'.format(twitch_data['stream']['viewers'])
        click.echo('%s is playing %s with %s viewers' % (name,game,viewers))

@cli.command(short_help='Launch livestreamer for a particular channel.')
@click.argument('channel')
@click.option('--quality', '-q', default='best')
@click.help_option('--help')
def watch(channel, quality):
    '''Launces livestreamer for a particular channel.'''
    launch_stream(channel, quality)

def launch_stream(channel, quality):
    if not can_connect_to_twitch():
        return
    streams = {}
    if os.path.isfile('streams_cache.json'):
        with open('streams_cache.json') as streams_file:
            streams = json.load(streams_file)
    if channel in streams:
        channel = streams[channel]
    call(['livestreamer', 'http://twitch.tv/' + channel, quality])

@cli.command(short_help='Check user followed channels.')
@click.argument('username')
@click.option('--setup')
def following(username):
    '''Lists a users followed streams'''
    print_following(username)

def print_following(username):
    if not can_connect_to_twitch():
        return
    url = 'https://api.twitch.tv/kraken/users/' + username + '/follows/channels'
    api_call = requests.get(url)
    if api_call.status_code == 404:
        click.echo('Error: not a valid user')
        return
    twitch_data = api_call.json()
    channels = []
    for stream in twitch_data['follows']:
        channel = stream['channel']['display_name']
        if is_online(channel):
            channels.append(channel)
    channels = sorted(channels)
    for c in channels:
        print_check(c)

def is_online(channel):
    if not can_connect_to_twitch:
        return
    url = 'https://api.twitch.tv/kraken/streams/' + channel
    api_call = requests.get(url)
    channel_data = api_call.json()
    if channel_data['stream'] == None:
        return False
    return True
