#!/usr/bin/node
// a script that reads and prints the content of a file;
var fs = require('fs');
const myArgs = process.argv.slice(2);

fs.readFile(myArgs[0], 'utf8', function(err, data){
	console.log(data);
});
