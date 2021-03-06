# Lurch

Lurch is a CLI for [twitch.tv](http://twitch.tv). It can do a few things, including listing the top channels that are currently live and checking the status of a single channel. Lurch also provides a simple interface into [livestreamer](https://github.com/chrippa/livestreamer) so that watching a stream from the terminal is quick and easy.

## Usage

```
Usage:
  lurch list [--number=<number>] [--game=<game>]
  lurch watch <channel> [--quality=<quality>]
  lurch check <channel>
  lurch (-h | --help | --version)

Options:
  -h --help            Show this screen.
  --version            Show version.
  --number=<number>    Number of streams to list from 1-100. [default: 25]
  --game=<name>        Name of game to list (lists all by default).
  --quality=<quality>  Livestreamer quality. [default: best]`
```

`$ lurch list` will list the top channels currently live on twitch.tv

By default Lurch will list the 25 most popular channels. This number can be increased or decreased with an optional number argument.

`$ lurch list --number 50`

The list can also be filtered by game with an optional argument. Use quotes for games with multi-worded names.

`$ lurch list --game "counter-strike: global offensive"`

Lurch also provides a shortcut to easily launch a stream with livestreamer.

```
$ lurch watch tsm_doublelift
```

Lurch can also check the status of a current channel.

```
$ lurch check nl_kripp
nl_kripp is online
```

## Installation

Lurch requires [livestreamer](http://docs.livestreamer.io/) in order to watch streams.

```
pip install livestreamer
npm install -g lurch
```

## License

MIT
