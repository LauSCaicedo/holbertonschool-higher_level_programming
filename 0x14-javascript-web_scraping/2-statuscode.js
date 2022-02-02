#!/usr/bin/node
const request = require('request');
const argument = process.argv[2];

request.get(argument, function (err, response){
  if (err) {
    console.log(err);
  }
  console.log('code: ' + response.statusCode);
});
