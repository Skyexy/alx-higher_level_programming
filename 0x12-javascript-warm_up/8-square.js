#!/usr/bin/node
const args = parseInt(process.argv[2]);
const si = 'X';
if (args) {
  for (let i = 0; i < args; i++) {
    console.log(si.repeat(args));
  }
} else {
  console.log('Missing size');
}
