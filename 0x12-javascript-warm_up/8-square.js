#!/usr/bin/node
const x = process.argv[2];
let y = '';
for (let i = 0; i < x; i++) {
  for (let j = 0; j < x; j++) {
    y += 'X';
  }
  y += '\n';
}
console.log(''.concat(...y));
