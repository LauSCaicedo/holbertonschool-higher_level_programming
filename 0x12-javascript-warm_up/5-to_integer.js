#!/usr/bin/node
const process = require('process');
const convert = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', convert);
}
