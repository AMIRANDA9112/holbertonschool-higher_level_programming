#!/usr/bin/node
const fileSystem = require('fs');
fileSystem.writeFileSync(process.argv[2], process.argv[3]);
