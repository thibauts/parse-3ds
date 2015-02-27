```javascript
var fs = require('fs');
var util = require('util');
var parse3DS = require('./');

var buf = fs.readFileSync('test.3ds');
var tree = parse3DS(buf);

console.log(util.inspect(tree, { depth: null }));
```