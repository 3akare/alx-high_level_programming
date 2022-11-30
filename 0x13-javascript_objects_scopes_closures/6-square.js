#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  print () {
    const array = [];
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        array.push('X');
      }
      console.log(array.join(''));
      array.length = 0;
    }
  }

  double () {
    this.size *= 2;
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      const array = [];
      for (let i = 0; i < this.size; i++) {
        for (let j = 0; j < this.size; j++) {
          array.push(c);
        }
        console.log(array.join(''));
        array.length = 0;
      }
    }
  }
};
