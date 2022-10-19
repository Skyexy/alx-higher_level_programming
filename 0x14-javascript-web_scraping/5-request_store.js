#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const fs = require('fs');
const request = require('request');
const link = myArgs[0];

request.get(link, (err, res, body) => {
  if (err) throw err;
  fs.writeFile(myArgs[1], body, 'utf8', function (err, data) {
    if (err) throw err;
  });
});
