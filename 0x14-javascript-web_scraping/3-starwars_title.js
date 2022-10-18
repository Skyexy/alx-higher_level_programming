#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const request = require('request');
var link = "https://swapi-api.hbtn.io/api/films/1/" + myArgs[0]
request.get( link, { json: true }, function (err, res, body) {
  console.log(body.title.statusCode);
});
