# Streams

<img src='https://cloud.githubusercontent.com/assets/9126138/6536575/e2fc822e-c40b-11e4-896e-a0c911030bfb.png' width="500px">

Streams is a CLI for [twitch.tv](http://twitch.tv). It can do a few things, including listing the top channels that are currently live and checking the status of a single stream. Streams also provides a simple interface into [livestreamer](https://github.com/chrippa/livestreamer) so that launching a stream from the terminal is quick and easy.

## Example Usage

`$ streams list` will list the top streams currently live on twitch.tv

By default Streams will list the 25 most popular streams. This number can be increased or decreased with an option number argument `-n` or `--number`

`$ streams list -n 50`

Streams can also check the status of a current channel. 

```
$ streams check nl_kripp
nl_kripp is playing Hearthstone: Heroes of Warcraft with 13,539 viewers.
```

Streams also provides a shortcut to easily launch a stream with livestreamer

```
$ streams watch nl_kripp
```

## Installation 

```
cd ~
git clone https://github.com/scwood/streams
cd streams 
python setup.py install
```

## License

MIT
