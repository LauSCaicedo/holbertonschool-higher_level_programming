#!/usr/bin/node
const { argv0 } = require('process');
const process = require('process');
convert = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', convert);
}
