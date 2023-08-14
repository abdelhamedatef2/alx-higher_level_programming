#!/usr/bin/node

const pro = process;

if (pro.argv.length < 3) {
  console.log('No argument');
} else if (pro.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
