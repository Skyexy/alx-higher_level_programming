#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  list.forEach(function(value){
    if (value == searchElement)
    {
      num = num + 1;
    }
  });
}
