#!/usr/bin/node

function factorial (Numb) {
  const num = Number(Numb);
  if (isNaN(num) === true | num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(process.argv[2]));
