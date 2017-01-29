import fetch from 'isomorphic-fetch';
import querystring from 'querystring';

class Twitch {

  constructor() {
    this.baseUrl = 'https://api.twitch.tv/kraken';
    this.headers = {
      accept: 'application/vnd.twitchtv.v5+json',
      'client-id': '2n7irufqjtyyayigyc4ubzq174axeex',
    };
  }

  async getStreams(number = null, game = null) {
    let url = `${this.baseUrl}/streams?`;
    const queryParams = {};
    if (number) {
      queryParams.number = number;
    }
    if (game) {
      queryParams.game = game;
    }
    url += querystring.stringify(queryParams);
    const { streams } = await this.fetchJsonWithHeaders(url);
    return streams;
  }

  async searchStreams(query) {
    let url = `${this.baseUrl}/search/streams?`;
    url += querystring.stringify({ limit: 100, query });
    const { streams } = await this.fetchJsonWithHeaders(url);
    return streams;
  }

  async fetchJsonWithHeaders(url, config = {}) {
    config.headers = Object.assign({}, config.headers, this.headers);
    const result = await fetch(url, config);
    return await result.json();
  }
}

export default new Twitch();
