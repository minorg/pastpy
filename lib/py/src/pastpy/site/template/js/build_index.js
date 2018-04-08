var lunr = require("./lunr.js");
var objects = require("./objects.js");

var idx = lunr(function () {
    this.ref("id");
    this.field("date");
    this.field("description");
    this.field("name");
    this.field("othername");
    this.field("title");

    objects.forEach(function (object) {
        this.add(object);
    }, this);
});

process.stdout.write(JSON.stringify(idx));
