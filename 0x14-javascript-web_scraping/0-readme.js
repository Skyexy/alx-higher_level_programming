#!/usr/bin/node

const myArgs = process.argv.slice(2);
const contents = readFileSync(myArgs[1], 'utf-8');
console.log(contents);
