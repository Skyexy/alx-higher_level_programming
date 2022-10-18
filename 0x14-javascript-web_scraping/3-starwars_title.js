#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const request = require('request');
var link = "https://swapi-api.hbtn.io/api/films/" + myArgs[0]

request.get(link, function (err, res, data) {
  console.log(data.title);
});
