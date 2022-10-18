#!/usr/bin/node
// a script that reads and prints the content of a file;
const fs = require('fs');
const myArgs = process.argv.slice(2);

fs.writeFile(myArgs[0], myArgs[1], 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  }
});
