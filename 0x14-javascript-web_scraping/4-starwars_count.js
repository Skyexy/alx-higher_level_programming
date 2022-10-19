#!/usr/bin/node
// a script that display the status code of a GET request;
const request = require('request');
const link = process.argv[2];;

request.get(link, { json: true }, (err, res, body) => {
  const bod = body.characters;
});
