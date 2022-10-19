#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const fs = {};
const request = require('request');
const link = myArgs[0];

request.get(link, (err, res, body) => {
  if (err) throw err;
  for (const resu of body) {
    if (resu.completed) {
      if (fs[resu.userId]) {
          fs[resu.userId]++
      }
      else {
        fs[resu.userId] = 1
      }
    }
  }
  console.log(fs);
});
