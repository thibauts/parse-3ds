var parse3DS = require('parse-3ds');
var fs = require('fs');
 
var buf = fs.readFileSync('./multi.3ds');
var parsed = parse3DS(buf, { 'objects':true, 'tree':false });

console.log(typeof parsed)
console.log(parsed)
