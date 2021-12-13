#!/usr/bin/node
const process = require('process');
const myVar = 2;
const myVar2 = 3;
if (process.argv.length <= myVar) {
  console.log('No argument');
} else if (process.argv.length === myVar2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
