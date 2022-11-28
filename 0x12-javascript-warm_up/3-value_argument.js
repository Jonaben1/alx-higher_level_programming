#!/usr/bin/node
const name = process.argv[2];
if (name) {
  console.log(name);
} else {
  console.log('No argument');
}
