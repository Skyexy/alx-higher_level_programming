#!/usr/bin/node
let args = 0;

if (process.argv[3]) {
  const me = process.argv.slice(2);
  me.sort(function (a, b) { return b - a; });
  args = me[1];
}
console.log(args);
