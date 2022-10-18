#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const request = require('request');

request.get("https://swapi-api.hbtn.io/api/films/1/", function (err, res, body) {
  console.log(body);
});
