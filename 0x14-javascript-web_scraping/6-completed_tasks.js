#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
const fs = {};
const request = require('request');
const link = myArgs[0];
var userid = 1;
var num = 0;
request.get(link, (err, res, body) => {
  if (err) throw err;
  for (const resu of body) {
    if (resu.completed) {
      if (userid[resu.userId]) {
          userid[resu.userId]++
      }
      else {
        userid[resu.userId] = 1
      }
    }
  }
  console.log(userid);
});
