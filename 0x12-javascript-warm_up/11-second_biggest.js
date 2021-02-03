#!/usr/bin/node
const Numbers = process.argv.slice(2);
if (process.argv.length <= 3) {
  console.log('0');
} else {
  Numbers.sort((a, b) => a - b);
  console.log(Numbers[Numbers.length - 2]);
}
