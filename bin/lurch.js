#!/usr/bin/env node

import fortyTwo from '../src/something';

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

console.log(doc);
