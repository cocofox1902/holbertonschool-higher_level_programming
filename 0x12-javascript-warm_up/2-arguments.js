#!/usr/bin/node
const process = require('process');

if (process.argv.length === 2) {
  console.log('None');
}
if (process.argv.length === 3) {
  console.log('Argument found');
}
if (process.argv.length === 4) {
  console.log('Arguments found');
}
