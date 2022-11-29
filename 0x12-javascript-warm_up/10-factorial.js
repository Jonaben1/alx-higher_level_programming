#!/usr/bin/node
function factorial (x) {
  if ((!x) || (x === 0)) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
const x = factorial(Number(process.argv[2]));
console.log(x);
