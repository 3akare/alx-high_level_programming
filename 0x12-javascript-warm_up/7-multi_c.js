#!/usr/bin/node

if (isNaN(process.argv[2])) { console.log('Missing number of occurrences'); } else {
  const number = parseInt(process.argv[2]);
  for (let i = 0; i < number; i++) { console.log('C is fun'); }
}
