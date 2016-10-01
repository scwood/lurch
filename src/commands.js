import childProcess from 'child_process';

import _ from 'lodash'
import fetch from 'isomorphic-fetch';

const twitchUrl = 'https://api.twitch.tv/kraken';
const headers = {
  accept: 'application/vnd.twitchtv[.version]+json',
  'client-id': '2n7irufqjtyyayigyc4ubzq174axeex'
}

function list(number) {

  function rowTemplate(number, name, viewers, game) {
    const numberColumns = 6;
    const nameColumns = 21;
    const viewersColumns = 13;
    const gameColumns = 38;
    number = _.padEnd(_.truncate(number, { length: numberColumns }), numberColumns)
    name = _.padEnd(_.truncate(name, { length: nameColumns }), nameColumns);
    viewers = _.padEnd(
      _.truncate(new Intl.NumberFormat().format(viewers), { length: viewersColumns }),
      viewersColumns);
    game = _.truncate(game, { length: gameColumns });
    return ` ${number}${name}${viewers}${game}\n`
  }

  let result = ''
  const seperator = '-'.repeat(79) + '\n';
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
      return result;
    });
}

function watch(channel, quality) {
  return childProcess.spawn('livestreamer', [`https://twitch.tv/${channel}`, quality]);
}

function check(channel) {
  return fetch(`${twitchUrl}/streams/${channel}`, { headers })
    .then(response => {
      if (response.status == 404) {
        return 'error: channel does not exist'
      }
      return response.json()
        .then(json => {
          if (json['stream'] == null) {
            return `${channel} is offline`
          }
          const game = json['stream']['game'];
          const viewers = new Intl.NumberFormat().format(json['stream']['viewers']);
          return `${channel} is playing ${game} with ${viewers} viewers`
        });
    });
}

export default { list, watch, check };
