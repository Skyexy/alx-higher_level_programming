#!/usr/bin/node

const {readFileSync, promises: fsPromises} = require('fs');
const myArgs = process.argv.slice(2);
const contents = readFileSync(myArgs[0], 'utf-8');
console.log(contents);
