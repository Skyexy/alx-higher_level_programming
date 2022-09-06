#!/usr/bin/node
function add(a, b){
	let z = a + b;
	console.log(z);
}
add(process.argv[2], process.argv[3]);
