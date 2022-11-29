#!/usr/bin/node
var myVar = 89;
var {myVar}  = require('./100-let_me_const');
console.log(myVar);
