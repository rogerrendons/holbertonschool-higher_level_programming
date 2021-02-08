#!/usr/bin/node

let Count = 0;
exports.logMe = function (item) {
  function printer (item) {
    console.log(Count + ': ' + item);
    Count++;
  }
  return printer(item);
};
