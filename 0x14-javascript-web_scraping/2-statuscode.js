#!/usr/bin/node
// a script that display the status code of a GET request;
const myArgs = process.argv.slice(2);
var request=require('request');

request.get(myArgs[0], function (err,res,body) {
  console.log("code: ", res.statusCode);
});
