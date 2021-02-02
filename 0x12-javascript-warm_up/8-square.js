#!/usr/bin/node
const Tam = process.argv[2];

if (isNaN(Tam)) {
  console.log('Missing size');
} else {
  for (let Square = 0; Square < Tam; Square++) {
    console.log('X'.repeat(Tam));
  }
}
