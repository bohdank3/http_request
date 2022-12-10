const jwt = require('jsonwebtoken');


module.exports = (data) => {

	var privateKey = fs.readFileSync('private.key');
	var token = jwt.sign({ foo: 'bar' }, privateKey, { algorithm: 'RS256'});
    
    data.token = token;
    return data;
};
