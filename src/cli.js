#!/usr/bin/env node

import { docopt } from 'docopt';

import pkg from '../package.json';

const doc = `Usage:
  lurch list [--number=<value>]
  lurch watch <channel> [--quality=<value>]
  lurch check <channel>
  lurch (-h | --help | --version)

Options:
  -h --help          Show this screen.
  --version          Show version.
  --number=<value>   Number of streams to list from 1-100. [default: 25]
  --quality=<value>  Livestreamer quality. [default: best]`

console.log(docopt(doc, { version: pkg.version }));
