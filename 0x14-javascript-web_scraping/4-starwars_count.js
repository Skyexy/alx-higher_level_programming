#!/usr/bin/node
// a script that display the status code of a GET request;
const request = require('request');
const myArgs = process.argv.slice(2);
const link = myArgs[0]
const count = 0;

request.get(link, { json: true }, (err, res, body) => {
  for (const resu of body.results) {
    for (const char of resu.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
