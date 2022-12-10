// build command: npm install jsonwebtoken

const moment = require("jsonwebtoken");

module.exports = (data) => {
    var m = moment;
    
    data.privateKey = m.fs.readFileSync('private.key');
    data.token = m.jwt.sign({ foo: 'bar' }, privateKey, { algorithm: 'RS256'});

    return data;

};
