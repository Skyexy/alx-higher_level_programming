#!/usr/bin/node
let args = 1;
if (process.argv[2]) {
  args = parseInt(process.argv[2]);
}
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const z = factorial(args);
console.log(z);
