#!/usr/bin/node
const fs = require('fs');
const argument = process.argv[2];

fs.readFile(argument, 'utf-8', function(err, data) {
  if (err) {
  console.log(err);
  }
  console.log(data);
});
