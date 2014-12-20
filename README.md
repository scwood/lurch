# Streams

Streams is a simple python script that will list the top 25 streams currently live on twitch.tv, sorted by popularity. When combined with [livestreamer](https://github.com/chrippa/livestreamer) it can provide a seamless twitch experience all from the terminal. 

## Usage

Requires python 3+ and [requests](http://docs.python-requests.org/en/latest/).

```
brew install python3
pip3 install requests
```

To use, download the script and add it to a directory in your PATH. Make executable by running `chmod +x streams`, and run at your leisure with `streams`.

If you want to take it further, add this function to your config file of the shell of your choice:

```
watch() {
    livestreamer twitch.tv/$1
}
```

Which boils the process of watching a twitch stream into:

```
streams
watch nl_kripp
```
