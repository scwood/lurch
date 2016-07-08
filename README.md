# Twinge

<img src='https://cloud.githubusercontent.com/assets/9126138/13517238/c1ca3650-e17e-11e5-8171-56d1c3cc924c.png'>

Twinge is a CLI for [twitch.tv](http://twitch.tv). It can do a few things, including listing the top channels that are currently live and checking the status of a single stream. Twinge also provides a simple interface into [livestreamer](https://github.com/chrippa/livestreamer) so that launching a stream from the terminal is quick and easy.

## Example Usage

`$ twinge list` will list the top streams currently live on twitch.tv

By default Twinge will list the 25 most popular streams. This number can be increased or decreased with an optional number argument `-n`.

`$ twinge list -n 50`

Twinge also provides a shortcut to easily launch a stream with livestreamer.

```
$ twinge watch nl_kripp
```

Twinge can also check the status of a current channel.

```
$ twinge check nl_kripp
nl_kripp is playing Hearthstone: Heroes of Warcraft with 13,539 viewers.
```

## Installation

With pip:

```
pip install twinge
```

Manually:

```
cd ~
git clone https://github.com/scwood/twinge
cd twinge
python setup.py install
```

## License

MIT
