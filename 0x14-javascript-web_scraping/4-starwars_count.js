#!/usr/bin/node
// a script that display the status code of a GET request;
const request = require('request');
const link = process.argv[2];;
const count = 0;

request.get(link, { json: true }, (err, res, body) => {
  for (const character of body.title) {
    if (character.includes('18')) {
      count++;
    }
  }
  console.log(count);
});
