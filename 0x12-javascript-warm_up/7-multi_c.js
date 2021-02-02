#!/usr/bin/node
const arg = parseInt(process.argv[2]);

if (isNaN(arg) === true) {
  console.log('Missing number of occurrences');
}
for (let Iter = 0; Iter < arg; Iter++) {
  console.log('C is fun');
}
