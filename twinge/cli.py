import click
import json
import requests
import sys

import twinge


@click.group()
@click.pass_context
def cli(context):
    '''Twinge is a CLI for Twitch.tv. Twinge can do a number of things
    including browsing the top channels, checking user followed channels,
    or checking the status of a particular channel. It also provides an easy
    shortcut into livestreamer to make launching twitch streams from the
    command line easy.
    '''
    context.obj = twinge.Client()


@cli.command(short_help='Lists the top live channels.')
@click.option('--number', '-n', default=25, required=False,
              type=click.IntRange(1, 100),
              help='Changes the number of channels to list.')
@click.pass_obj
def list(client, number):
    '''Lists the top channels that are currently live on twitch sorted by
    number of viewers.
    '''
    try:
        channels = client.get_online_channels(number)
    except ConnectionError as e:
        sys.exit(e)
    line_size = 79
    number_columns = 5
    name_columns = 22
    viewers_columns = 11
    game_size = 41
    header = '{0:<%d}{1:<%d}{2:<%d}' % (
        number_columns, name_columns, viewers_columns)
    content = '{0:<%d}{1:<%d}{2:<%d,}' % (
        number_columns, name_columns, viewers_columns)
    print('-' * line_size)
    print(header.format(' #', 'channel', 'viewers') + 'game')
    print('-' * line_size)
    def truncate(string, length):
        if string is None:
            return 'None'
        elif len(string) <= length:
            return string
        else:
            return string[0:length-3] + '...'
    for i, c in enumerate(channels):
        number = ' ' + str(i+1) + '.'
        name = truncate(c['name'], name_columns-1)
        viewers = c['viewers']
        game = truncate(c['game'], game_size-1)
        print(content.format(number, name, viewers) + game)


@cli.command(short_help='Checks the status of a single channel.')
@click.argument('channel')
def check(channel):
    '''This will check if a particular channel is currently online or not,
    and if it is will provide additional information.
    '''
    print_check(channel)


def print_check(channel):
    url = 'https://api.twitch.tv/kraken/streams/' + channel
    api_call = requests.get(url)
    twitch_data = api_call.json()
    if 'Error' in twitch_data:
        print('Error: ' + channel + ' is not a valid channel name')
    elif twitch_data['stream'] == None:
        print(channel + ' is offline')
    else:
        name = twitch_data['stream']['channel']['display_name']
        game = twitch_data['stream']['game']
        viewers = '{:,}'.format(twitch_data['stream']['viewers'])
        print('%s is playing %s with %s viewers' % (name, game, viewers))


@cli.command(short_help='Launch livestreamer for a particular channel.')
@click.argument('channel')
@click.option('--quality', '-q', default='best')
@click.pass_obj
def watch(client, channel, quality):
    '''Launches livestreamer for a particular channel.'''
    client.watch_channel(channel, quality)


# @cli.command(short_help='Check user followed channels.')
# @click.argument('username')
# def following(username):
#     '''Lists a users followed streams'''
#     print_following(username)


def print_following(username):
    url = 'https://api.twitch.tv/kraken/users/' + username + '/follows/channels'
    api_call = requests.get(url)
    if api_call.status_code == 404:
        print('Error: not a valid user')
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
    url = 'https://api.twitch.tv/kraken/streams/' + channel
    api_call = requests.get(url)
    channel_data = api_call.json()
    if channel_data['stream'] == None:
        return False
    return True
