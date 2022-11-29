#!/usr/bin/node
const x = process.argv[2];
let i = 0;
while (i < x) {
  console.log(''.concat(...'C is fun'));
  i++;
}
if (!x) {
  console.log(''.concat(...'Missing number of occurrences'));
}
