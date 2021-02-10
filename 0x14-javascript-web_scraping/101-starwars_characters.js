#!/usr/bin/node

const request = require('request');
const args = process.argv[2];

request('https://swapi-api.hbtn.io/api/films/' + args, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const film = JSON.parse(body);
  for (const char in film.characters) {
    request(film.characters[char], function (error, response, body) {
      if (error) {
        console.log(error);
      } else {
        const aChar = JSON.parse(body);
        console.log(aChar.name);
      }
    });
  }
});
