#!/usr/bin/node
const process = require('process');
const size = process.argv[2];
let z, y;
let esp = '';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}

for (z = 0; z < size; z++) {
  for (y = 0; y < size; y++) {
    esp += 'X';
  }
  esp += '\n';
}
console.log(esp);
