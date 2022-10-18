#!/usr/bin/node
// a script that reads and prints the content of a file;
var fs = require('fs');

function asyncReadFile(filename){
	try {
		const contents = fs.readFile(filename, 'utf-8');

		console.log(contents);
	} catch (err) {
		console.log(err);
	}
}

const myArgs = process.argv.slice(2);
asyncReadFile(myArgs[0]);
