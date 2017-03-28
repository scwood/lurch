import fetch from 'isomorphic-fetch';
import querystring from 'querystring';

const baseUrl = 'https://api.twitch.tv/kraken';
const headers = {
  accept: 'application/vnd.twitchtv.v5+json',
  'client-id': '2n7irufqjtyyayigyc4ubzq174axeex',
}

async function getStreams(limit = null, game = null) {
  let url = `${baseUrl}/streams?`;
  const queryParams = {};
  if (limit) {
    queryParams.limit = limit;
  }
  if (game) {
    queryParams.game = game;
  }
  url += querystring.stringify(queryParams);
  const { streams } = await fetchJsonWithHeaders(url);
  return streams;
}

async function searchStreams(query) {
  let url = `${baseUrl}/search/streams?`;
  url += querystring.stringify({ limit: 100, query });
  const { streams } = await fetchJsonWithHeaders(url);
  return streams;
}

async function fetchJsonWithHeaders(url, config = {}) {
  config.headers = Object.assign({}, config.headers, headers);
  const result = await fetch(url, config);
  return await result.json();
}

export default { getStreams, searchStreams };
