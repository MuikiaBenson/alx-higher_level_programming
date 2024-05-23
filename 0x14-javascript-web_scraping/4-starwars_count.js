#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      if (film.characters.includes(characterUrl)) {
        count++;
      }
    }
    console.log(count);
  } else {
    console.log('An error occurred. Status code: ' + response.statusCode);
  }
});
