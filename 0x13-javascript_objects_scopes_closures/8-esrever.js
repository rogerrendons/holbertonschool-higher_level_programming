#!/usr/bin/node

exports.esrever = function (list) {
  const ListNew = [];
  for (let Iter = list.length - 1; Iter >= 0; Iter--) {
    ListNew.push(list[Iter]);
  }
  return ListNew;
};
