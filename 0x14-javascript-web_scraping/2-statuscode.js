#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const https = require('https');

https.request(myArgs[0], function (response) {
  console.log("code: ", response.statusCode);
});
