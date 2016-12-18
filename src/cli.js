#!/usr/bin/env node

import { docopt } from 'docopt';

import commands from './commands.js';
import pkg from '../package.json';

const usage = `Usage:
  lurch list [--number=<value>]
  lurch watch <channel> [--quality=<value>]
  lurch check <channel>
  lurch (-h | --help | --version)

Options:
  -h --help          Show this screen.
  --version          Show version.
  --number=<value>   Number of streams to list from 1-100. [default: 25]
  --quality=<value>  Livestreamer quality. [default: best]`;

const options = docopt(usage, { version: pkg.version });

if (options['list']) {
  commands.list(options['--number']).then(result => console.log(result));
} else if (options['watch']) {
  const process = commands.watch(options['<channel>'], options['--quality']);
  process.stdout.on('data', data => console.log(data.toString()));
  process.stderr.on('data', data => console.log(data.toString()));
} else if (options['check']) {
  commands.check(options['<channel>']).then(result => console.log(result));
}
