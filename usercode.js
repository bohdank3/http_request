// build command: npm install jsonwebtoken

const moment = require("jsonwebtoken");

module.exports = (data) => {
    data.privateKey = fs.readFileSync('private.key');
    data.token = jwt.sign({ foo: 'bar' }, privateKey, { algorithm: 'RS256'});

    return data;

};