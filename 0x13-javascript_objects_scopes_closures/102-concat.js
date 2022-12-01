#!/usr/bin/node

const fs = require('fs');
let string;

fs.readFile(process.argv[2], (err, data) => {
  if (err) throw err;
  string += data.toString();
});

console.log(string);
// fs.readFile("./main.js", (err, data) =>{
//     if (err) throw err;
//     console.log(data.toString());
// })

// fs.writeFile('new.txt', "content", err=>{
//     if (err) throw err;
// })
