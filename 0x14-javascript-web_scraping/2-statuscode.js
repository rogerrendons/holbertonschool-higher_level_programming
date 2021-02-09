#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, resp) => {
  if (err) {
    console.error('code: ', err);
  } else {
    console.log('code:', resp && resp.statusCode);
  }
});
