#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
const count = 0;

request.get(link, { json: true }, (err, res, body) => {
  for (const character of body.title) {
    if (character.includes('18')) {
      count++;
    }
  }
  console.log(count);
});
