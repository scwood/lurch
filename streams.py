import click
import requests

# TODO add command to get live streams from a persons follows list

def can_connect_to_twitch():
    try:
        check = requests.get('http://www.twitch.tv/')
        return True
    except requests.ConnectionError:
        click.echo('error: can\'t reach twitch.tv')
    return False

def trim(string, length):
    if string is None:
        return 'None'
    elif len(string) <= length:
        return string
    else: 
        return string[0:length - 3] + '...'

@click.group()
@click.help_option('-h', '--help')
def cli():
    '''This script does twitch stuff.'''
    pass

@cli.command(short_help='Lists the top live channels.')
@click.help_option('-h', '--help')
@click.option('--number', '-n', default=25, required=False,
        type=click.IntRange(1, 100), 
        help='Changes the number of channels to list.')
def list(number):
    '''This will list the top channels that are currently live on twitch
    sorted by number of viewers.
    '''
    if not can_connect_to_twitch():
        return
    url = 'https://api.twitch.tv/kraken/streams?limit=' + str(number)
    api_call = requests.get(url)
    twitch_data = api_call.json()  
    streams = twitch_data['streams']
    line_size = 79
    number_size = 5
    name_size = 22
    viewers_size = 11
    game_size = 41
    header = '{0:<%d}{1:<%d}{2:<%d}' % (number_size, name_size, viewers_size)
    content = '{0:<%d}{1:<%d}{2:<%d,}' % (number_size, name_size, viewers_size)
    click.echo('-' * line_size)
    click.echo(header.format(' #','channel','viewers') + 'game')
    click.echo('-' * line_size)
    for x in range(0, len(streams)):
        number = ' ' + str(x + 1) + '.'
        name = trim(streams[x]['channel']['name'], name_size - 1)
        viewers = streams[x]['viewers']
        game = trim(streams[x]['game'], game_size - 1)
        click.echo(content.format(number, name, viewers) + game)

@cli.command(short_help='Checks the status of a single channel.')
@click.argument('channel')
@click.help_option('-h', '--help')
def check(channel):
    '''This will check if a particular channel is currently online or not,
    and if it is will provide additional information.
    '''
    if not can_connect_to_twitch():
        return
    url = 'https://api.twitch.tv/kraken/streams/' + channel
    api_call = requests.get(url)
    twitch_data = api_call.json()
    if 'error' in twitch_data:
        click.echo('error:', channel, 'is not a valid stream name')
    elif twitch_data['stream'] == None:
        click.echo(channel, 'is offline')
    else:
        game = twitch_data['stream']['game']
        viewers = '{:,}'.format(twitch_data['stream']['viewers'])
        click.echo('%s is playing %s with %s viewers' % (channel,game,viewers))

# @cli.command()
# @click.argument('channel')
# @click.option('--quality', '-q', default='best')
# @click.help_option('-h', '--help')
# def watch(channel, quality):
#     if not can_connect_to_twitch():
#         return
#     call(['livestreamer', 'http://twitch.tv/' + str(channel), quality])
