#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('No argument');
}else {
	const args = process.argv.slice(2);
	args.forEach((val, index) => {
		console.log(val);
	});
}
