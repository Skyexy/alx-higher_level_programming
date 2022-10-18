#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const https = require('https');

request.on(myArgs[0], function (res) {
  console.log("code: ", res.statusCode);
});
