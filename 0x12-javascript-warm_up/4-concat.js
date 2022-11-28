#!/usr/bin/node
const lists = [process.argv[2], ' ', 'is', ' ', process.argv[3]];
const result = ''.concat(...lists);
console.log(result);
