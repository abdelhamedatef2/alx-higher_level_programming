#!/usr/bin/node

const x = process.argv[2];
const num = Number.parseInt(x);

if (num) {
  for (let i = 0; i < num; i++) {
    let text = '';
    for (let j = 0; j < num; j++) {
      text += 'X';
    }
    console.log(text);
  }
} else {
  console.log('Missing size');
#!/usr/bin/node

const x = process.argv[2];
const num = Number.parseInt(x);

if (num) {
  for (let i = 0; i < num; i++) {
    let text = '';
    for (let j = 0; j < num; j++) {
      text += 'X';
    }
    console.log(text);
  }
} else {
  console.log('Missing size');
}}
