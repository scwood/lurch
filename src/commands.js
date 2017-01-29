import _ from 'lodash';
import childProcess from 'child_process';

import twitch from './twitch';

async function list(number = null, game = null) {
  const seperator = '-'.repeat(80);
  let result = [];
  result.push(seperator);
  result.push(rowTemplate('#', 'name', 'viewers', 'game'));
  result.push(seperator);
  const streams = await twitch.getStreams(number, game);
  const rows = streams.map((stream, i) => {
    const { channel: { name }, viewers, game } = stream;
    return rowTemplate(i + 1, name, viewers, game);
  });
  return result.concat(rows).join('\n');
}

function rowTemplate(number, name, viewers, game) {
  const numberColumns = 6;
  const nameColumns = 21;
  const viewersColumns = 13;
  const gameColumns = 40;
  const paddedNumber = _.padEnd(
    _.truncate(number, { length: numberColumns }), numberColumns);
  const paddedName = _.padEnd(
    _.truncate(name, { length: nameColumns }), nameColumns);
  const paddedViewers = _.padEnd(
    typeof(number) === 'number'
      ? _.truncate(
        new Intl.NumberFormat().format(viewers), {
          length: viewersColumns
        })
      : viewers, viewersColumns);
  const truncatedGame = _.truncate(game, { length: gameColumns });
  return ` ${paddedNumber}${paddedName}${paddedViewers}${truncatedGame}`;
}

async function check(channelName) {
  const streams = await twitch.searchStreams(channelName);
  const found = streams.find(stream => {
    return stream.channel.display_name === channelName;
  });
  if (found === undefined) {
    return `${channelName} is offline or doesn't exist`;
  }
  const game = found['game'];
  const viewers = new Intl.NumberFormat().format(found['viewers']);
  return `${channelName} is playing ${game} with ${viewers} viewers`;
}

function watch(channel, quality) {
  return childProcess.spawn(
    'livestreamer', [`https://twitch.tv/${channel}`, quality]);
}

export default { list, watch, check };
