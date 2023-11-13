#!/usr/bin/node

function addMeMaybe (number, thefunction) {
  return thefunction(++number);
}

module.exports.addMeMaybe = addMeMaybe;