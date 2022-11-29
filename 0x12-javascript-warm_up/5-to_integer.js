#!/usr/bin/node
const myNum = process.argv[2];
const num = 'My number:';
if (!Number(myNum)) {
  console.log(''.concat(...'Not a number'));
} else {
  console.log(''.concat(...num, ' ', myNum));
}
