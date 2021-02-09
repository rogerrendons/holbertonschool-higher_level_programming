#!/usr/bin/node

const request = require('request');
const args = process.argv;
let Acum = 0;

request(args[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    for (const List in films) {
      for (const Charac in films[List].characters) {
        if (films[List].characters[Charac].includes('/18/')) {
          Acum++;
        }
      }
    }
  }
  return console.log(Acum);
});
