#!/usr/bin/node
// a script that reads and prints the content of a file;
async function asyncReadFile(filename){
	try {
		const contents = await fsPromises.readFile(filename, 'utf-8');

		console.log(contents);
	} catch (err) {
		console.log(err);
	}
}

const myArgs = process.argv.slice(2);
asyncReadFile(myArgs[0]);
