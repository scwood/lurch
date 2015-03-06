# Streams

<img src='https://cloud.githubusercontent.com/assets/9126138/6536575/e2fc822e-c40b-11e4-896e-a0c911030bfb.png' width="500px">

Streams is a python script that will list the top 25 streams currently live on twitch.tv, sorted by popularity. When combined with [livestreamer](https://github.com/chrippa/livestreamer) it can provide a seamless twitch experience all from the terminal. 

## Usage

Requires python 3 and [requests](http://docs.python-requests.org/en/latest/).

On OSX:

```
brew install python3
pip3 install requests
```

For other operating systems replace `brew` with the package manager of your choice.

To use, download the script and add it to a directory in your PATH. Make executable by running `chmod +x streams`, and run at your leisure with the command `streams`.

If you want to take it further, add this function or something similar to your .bashrc.

```
watch() {
    livestreamer twitch.tv/$1 best
}
```

Which boils the process of watching a twitch stream down to:

```
streams
watch nl_kripp
```

## License

MIT
