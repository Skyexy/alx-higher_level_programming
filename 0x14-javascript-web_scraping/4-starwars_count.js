#!/usr/bin/node
// a script that display the status code of a GET request;
const request = require('request');
const myArgs = process.argv.slice(2);
const link = myArgs[0];
let count = 0;

request.get(link, { json: true }, (err, res, body) => {
  if (err) throw err;
  for (const resu of body.results) {
    for (const char of resu.characters) {
      if (char.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
