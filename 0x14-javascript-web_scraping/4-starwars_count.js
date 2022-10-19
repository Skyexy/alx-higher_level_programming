#!/usr/bin/node
// a script that display the status code of a GET request;
const request = require('request');
var link = "https://swapi-api.hbtn.io/api/people/18/"

request.get( link, { json: true }, (err,res,body) => {
  var bod = body.films;
  console.log(bod.length);
});
