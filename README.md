# Seize

<img src='https://cloud.githubusercontent.com/assets/9126138/16828648/ef17e534-494e-11e6-9716-ff95d2e40d67.png'>

Seize is a CLI for [twitch.tv](http://twitch.tv). It can do a few things, including listing the top channels that are currently live and checking the status of a single stream. Seize also provides a simple interface into [livestreamer](https://github.com/chrippa/livestreamer) so that launching a stream from the terminal is quick and easy.

## Example Usage

`$ seize list` will list the top streams currently live on twitch.tv

By default Seize will list the 25 most popular streams. This number can be increased or decreased with an optional number argument `--number`.

`$ seize list --number 50`

Seize also provides a shortcut to easily launch a stream with livestreamer.

```
$ seize watch tsm_doublelift
```

Seize can also check the status of a current channel.

```
$ seize check nl_kripp
nl_kripp is playing Hearthstone: Heroes of Warcraft with 13,539 viewers.
```

## Installation

Seize requires [livestreamer](http://docs.livestreamer.io/) in order to watch streams.

```
pip install livestreamer
gem install seize
```

## License

MIT
