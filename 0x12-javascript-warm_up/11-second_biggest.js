#!/usr/bin/node

const numbers = process.argv.slice(2).map(a => parseInt(a, 10)).sort((a, b) => b - a);

if (!numbers.length || numbers.length === 1) {
  console.log(0);
} else {
  console.log(numbers[1]);
}
