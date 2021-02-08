#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let Iter;
  let Acum = 0;
  for (Iter = 0; Iter < list.length; Iter++) {
    if (list[Iter] === searchElement) {
      Acum++;
    }
  }
  return Acum;
};
