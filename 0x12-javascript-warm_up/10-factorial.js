#!/usr/bin/node
if (isNaN(process.argv[2])){
  const args = 1;
}
else {
  const args = parseInt(process.argv[2]);
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
