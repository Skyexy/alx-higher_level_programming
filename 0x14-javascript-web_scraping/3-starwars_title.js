#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];

request.get(link, { json: true }, (err, res, body) => {
  if (err) throw err;
  console.log(body.title);
});
