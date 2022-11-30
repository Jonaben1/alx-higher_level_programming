#!/usr/bin/node
const args = process.argv.splice(2);
if ((args.length === 0) || (args.length === 1)) {
  console.log(0);
} else {
  console.log(second(args));
}

function second (arg) {
  let first = arg[0];
  let sec = arg[1];
  for (const x in arg) {
    if (arg[x] > first) {
      first = arg[x];
    }
    for (const x in arg) {
      if ((arg[x] > sec) && (arg[x] < first)) {
        sec = arg[x];
      }
    }
  }
  return sec;
}
