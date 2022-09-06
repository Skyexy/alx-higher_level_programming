#!/usr/bin/node
function add (a, b) {
  const z = a + b;
  console.log(z);
}
const args = parseInt(process.argv[2]);
const args2 = parseInt(process.argv[3]);
add(args, args2);
