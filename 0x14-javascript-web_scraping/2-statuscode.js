#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const request = require('request');

request.get(myArgs[0], function (err, res, data) {
  console.log('code:', res.statusCode);
});
