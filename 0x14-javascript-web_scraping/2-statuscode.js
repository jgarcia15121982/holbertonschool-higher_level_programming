#!/usr/bin/node

const myURL = process.argv[2];
const request = require('request');

request(myURL, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: %d', response.statusCode);
  }
});
