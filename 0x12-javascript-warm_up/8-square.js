#!/usr/bin/node
const process = require('process');
const size = process.argv[2];
let z;

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}

for (z = 0; z < size; z++) {
  console.log('X'.repeat(size));
}
