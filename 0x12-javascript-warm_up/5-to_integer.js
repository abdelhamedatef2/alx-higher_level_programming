#!/usr/bin/node

const argv = process.argv;

const num = Number.parseInt(argv[2]);
if (num) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
