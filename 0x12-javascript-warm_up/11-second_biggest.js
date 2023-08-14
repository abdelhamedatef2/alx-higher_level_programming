#!/usr/bin/node

const argv = process.argv;

if (argv.length < 4) {
  console.log(0);
} else {
  const arr = argv.map(el => Number.parseInt(el))
    .filter(el => !Number.isNaN(el));
  const fArr = arr.filter(el => el !== Math.max(...arr));
  console.log(Math.max(...fArr));
}
