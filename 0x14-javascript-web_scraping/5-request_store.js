#!/usr/bin/node

const request = require('request');
const myFile = require('fs');

request(process.argv[2], (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    myFile.writeFile(process.argv[3], body, 'utf-8', (err, data) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
