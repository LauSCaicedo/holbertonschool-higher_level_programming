#!/usr/bin/node
const fs = require('fs');
const argument = process.argv[2];
const text = process.argv[3];

fs.writeFile(argument, text, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
