#!/usr/bin/node
const request = require('request');
const argument = process.argv[2];
const page = 'https://swapi-api.hbtn.io/api/films/' + argument;

request.get(page, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
