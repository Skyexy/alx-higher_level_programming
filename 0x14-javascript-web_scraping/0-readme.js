#!/usr/bin/node

try {

	const myArgs = process.argv.slice(2);
	
	const contents = await fsPromises.readFile(myArgs[0], 'utf-8');
	
	console.log(contents);
} catch (err) {
	console.log(err);
}
