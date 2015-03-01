parse-3ds
=========
### Parses 3D Studio .3DS files

Parses 3DS files and returns objet data. The full 3DS chunk tree is parsed internally, allowing to easily extend the module and provide parsers for various chunk types.

Install
-------

```bash
$ npm install parse-3ds
```

Usage
-----

```javascript
var parse3DS = require('parse-3ds');
var fs = require('fs');

var buf = fs.readFileSync('test.3ds');
var parsed = parse3DS(buf);

/*
{ 
  objects: [ 
    { name: 'a', vertices: [ ... ], faces: [ ... ] },
    { name: 'b', vertices: [ ... ], faces: [ ... ] },
    { name: 'c', vertices: [ ... ], faces: [ ... ] }
  ]
}
*/
```
