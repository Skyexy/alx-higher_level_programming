#!/usr/bin/node
let z = 1;
const args = parseInt(process.argv[2]);
if (args === 0 || args === 1 || isNAN(args)) {
  console.log(z);
} else {
  for (let i = args; i >= 1; i--) {
    z = z * i;
  }
  console.log(z);
}
