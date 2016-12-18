import _ from 'lodash';
import childProcess from 'child_process';
import fetch from 'isomorphic-fetch';

const twitchUrl = 'https://api.twitch.tv/kraken';
const headers = {
  accept: 'application/vnd.twitchtv[.version]+json',
  'client-id': '2n7irufqjtyyayigyc4ubzq174axeex'
};

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
  return ` ${paddedNumber}${paddedName}${paddedViewers}${truncatedGame}\n`;
}

function list() {
  let result = '';
  const seperator = '-'.repeat(80) + '\n';
  result += seperator;
  result += rowTemplate('#', 'name', 'viewers', 'game');
  result += seperator;
  return fetch(`${twitchUrl}/streams`, { headers })
    .then(response => response.json())
    .then(json => {
      json['streams'].forEach((stream, i) => {
        result += rowTemplate(i + 1,
          stream['channel']['name'],
          stream['viewers'],
          stream['game']);
      });
      return result.slice(0, -2);
    });
}

function watch(channel, quality) {
  return childProcess.spawn(
    'livestreamer', [`https://twitch.tv/${channel}`, quality]);
}

function check(channel) {
  return fetch(`${twitchUrl}/streams/${channel}`, { headers })
    .then(response => {
      if (response.status == 404) {
        return 'channel does not exist';
      }
      return response.json()
        .then(json => {
          if (json['stream'] == null) {
            return `${channel} is offline`;
          }
          const game = json['stream']['game'];
          const viewers = new Intl.NumberFormat().format(
            json['stream']['viewers']);
          return `${channel} is playing ${game} with ${viewers} viewers`;
        });
    });
}

export default { list, watch, check };
