#!/usr/bin/node

const request = require('request');
const endPoint = 'https://swapi-api.hbtn.io/api/films/';
const url = endPoint + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
