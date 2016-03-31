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

### parsed = require('parse-3ds')(buf[, options]) ###

Returns the parsed contents of `buf`. `options`, if present, can contain the following keys:
* `objects`: if `true`, object data will be available. Default is `true`.
* `tree`: if `true`, the full chunks tree will be available. Default is `false`.
* `encoding`: the encoding used to interpret strings stored in parsed file. Defaults to `binary` (latin-1).

Note: should you need to explicitly set `encoding`, please consider logging an issue for further investigation.

Example
-------

```javascript
var parse3DS = require('parse-3ds');
var fs = require('fs');

var buf = fs.readFileSync('test.3ds');
var parsed = parse3DS(buf, { 'objects':true, 'tree':true });

/*
{ 
  objects: [ 
    { name: 'a', vertices: [ ... ], faces: [ ... ] },
    { name: 'b', vertices: [ ... ], faces: [ ... ] },
    { name: 'c', vertices: [ ... ], faces: [ ... ] }
  ],
  tree: [
    // Unparsed nodes will have an extra 'data' field
    { id: 42, length: 42, name: 'abc', children: [ ... ] }
  ]
}
*/
```
