#!/usr/bin/node
const process = require('process');
const size = parseInt(process.argv[2]);
let z;

if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
for (z = 0; z < size; z++) {
  console.log('X'.repeat(size));
}
