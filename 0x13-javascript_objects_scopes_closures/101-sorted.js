#!/usr/bin/node
const data = require('./101-data.js').dict;
const ocurrences = {};
for (const key in data) {
  const idx = data[key];
  if (ocurrences[idx] === undefined) {
    ocurrences[idx] = [];
  }
  ocurrences[idx].push(key);
}

console.log(ocurrences);
