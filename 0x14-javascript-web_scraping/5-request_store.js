#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const request = require('request');
var link = myArgs[0]

request.get(link, { json: true }, (err, res, body) => {
  fs.writeFile(myArgs[1], body, 'utf8', function (err, data) {
    if (err) {
      console.error(err);
    }
  });
});
