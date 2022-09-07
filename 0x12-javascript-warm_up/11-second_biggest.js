#!/usr/bin/node
let args = 0;

if (process.argv[3]){
  let me = process.argv.slice(2);
  me.sort(function(a, b){return a - b});
  args = me[1];
}
console.log(args);
