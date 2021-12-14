#!/usr/bin/node
const process = require('process');
const x = process.argv[2];
let z = 0;
while (z < x) {
  console.log('C is fun');
  z++;
}
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}
