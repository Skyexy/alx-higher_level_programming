#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/people/18/';

request.get(link, { json: true }, (err, res, body) => {
  const bod = body.films;
  console.log(bod.length);
});
