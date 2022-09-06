#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('No argument');
}else {
	process.argv.forEach((val, index) => {
		console.log(val[:3]);
	});
}
