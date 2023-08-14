#!/usr/bin/node

const pro = process;

if (pro.argv[2]) {
  console.log(pro.argv[2]);
} else {
  console.log('No argument');
}
