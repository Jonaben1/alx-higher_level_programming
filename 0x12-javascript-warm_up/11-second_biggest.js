#!/usr/bin/node
let args = process.argv.slice(2);
if ((!args) || (args ===1)) {
  console.log(0);
} else {
  console.log(second(args));
}

function second (arg) {
  const first = arg[0];
  const sec  = arg[0];
  for (let x in arg) {
    if (arg[x] > first) {
      first = arg[x];
    }
      for (let x in arg) {
        if ((arg[x] > sec) && (arg[x] < first)) {
          sec = arg[x];
        }
      }
  return sec;
}
}
