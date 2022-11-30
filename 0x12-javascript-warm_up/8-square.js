#!/usr/bin/node
const myVar = 'X';
const myArgs = process.argv.splice(2);
const num = Number(myArgs[0]);
if (!num) {
  console.log('Missing size');
} else {
  myString = '';
  for (let i = 0; i < num; i++) {
    myString += myVar;
  }
  for (let i = 0; i < num; i++) {
    console.log(myString);
  }
}
