#!/usr/bin/node
const { readFile, appendFileSync } = require('fs');
const [fileA, fileB, outputFile] = process.argv.slice(2);

readFile(fileA, (err, data) => {
  if (err) throw err;
  appendFileSync(outputFile, data);
});

readFile(fileB, (err, data) => {
  if (err) throw err;
  appendFileSync(outputFile, data);
});
