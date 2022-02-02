#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argument = process.argv[2];
const sArgument = process.argv[3];

request.get(argument, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(sArgument, body, function (error) {
      if (error) {
        console.log(err);
      }
    });
  }
});
