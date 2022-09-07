#!/usr/bin/node
let args = 0;
if (process.argv[3]){
  args = process.argv.slice(2);
  args.sort(function(a, b){return a - b});
  args = args[1];
}
console(args);
