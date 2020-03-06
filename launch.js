var parse3DS = require('parse-3ds');
var fs = require('fs');
 
var buf = fs.readFileSync('./multi.3ds');
var parsed = parse3DS(buf, { 'objects':true, 'tree':false });
var parsed = parsed["objects"];

//wipe clean
//fs.writeFileSync("vertices.txt","");
//fs.writeFileSync("faces.txt","");

console.log(parsed)
console.log(typeof(parsed))

JSONer = JSON.stringify(parsed)

fs.writeFileSync("./everything.json",JSONer);

/*
LEGACY .TXT WRITER, NEEDS POST PROCESSING TO IMPORT INTO PYTHON. JSON PREFERED ABOVE.
for (var i = 0; i < parsed.length; i++){
    console.log(parsed[i]);
    fs.appendFileSync("vertices.txt",parsed[i].name+"\n");
    fs.appendFileSync("faces.txt",parsed[i].name+"\n");
    for (var k = 0; k < parsed[i].noVertices; k++){
        fs.appendFileSync("vertices.txt","    "+parsed[i].vertices[k]+"\n");
    }
    for (var k = 0; k < parsed[i].noFaces; k++){
        fs.appendFileSync("faces.txt","    "+parsed[i].faces[k]+"\n");
    }
}
*/
