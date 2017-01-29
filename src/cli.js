#!/usr/bin/env node

import { docopt } from 'docopt';

import commands from './commands.js';
import pkg from '../package.json';

async function main() {
  const usage = `Usage:
    lurch list [--number=<value>] [--game=<gamename>]
    lurch watch <channel> [--quality=<value>]
    lurch check <channel>
    lurch (-h | --help | --version)

  Options:
    -h --help          Show this screen.
    --version          Show version.
    --number=<value>   Number of streams to list from 1-100. [default: 25]
    --game=<gamename>  Name of game to list (lists all by default).
    --quality=<value>  Livestreamer quality. [default: best]`;
  const options = docopt(usage, { version: pkg.version });
  if (options['list']) {
    console.log(await commands.list(options['--number'], options['--game']));
  } else if (options['watch']) {
    const watchProcess = commands.watch(
      options['<channel>'], options['--quality']);
    watchProcess.stdout.on('data', data => console.log(data.toString()));
    watchProcess.stderr.on('data', data => console.log(data.toString()));
  } else if (options['check']) {
    console.log(await commands.check(options['<channel>']));
  }
}

if (!module.parent) {
  try {
    main();
  } catch (error) {
    console.log(error);
  }
}
