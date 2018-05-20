var lunr = require("./lunr.min.js");
var objects = require("./objects.js");

var idx = lunr(function () {
    this.ref("id");
    this.field("date");
    this.field("description");
    this.field("name");
    this.field("othername");
    this.field("title");

    for (var objectId in objects) {
        this.add(objects[objectId]);
    }
});

process.stdout.write(JSON.stringify(idx));
