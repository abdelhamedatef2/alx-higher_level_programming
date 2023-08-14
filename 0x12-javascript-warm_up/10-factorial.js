#!/usr/bin/node

const num = Number.parseInt(process.argv[2]);

let x = 1;
if (num) {
  x = num;
}

function fact (n) {
  if (n > 0) {
    return (n * fact(n - 1));
  }
  return (1);
}

console.log(fact(x));
