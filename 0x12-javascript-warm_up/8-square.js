#!/usr/bin/node
const args = parseInt(process.argv[2]);
if (args) {
  for (let i = 0; i < args; i++) {
    for (let i = 0; i < args; i++){
      console.log('X');
    }
  }
} else {
  console.log('Missing size');
}
