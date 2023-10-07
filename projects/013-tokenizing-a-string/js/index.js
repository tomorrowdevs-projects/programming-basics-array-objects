function toToken(expression) {

    const tokenPattern = /[*\/^\-+\()\[\]\{\}]|[0123456789]+/g;

    const tokenCollection = expression.match(tokenPattern);

    return tokenCollection;
}

const prompt = require('prompt-sync')({sigint: true});

const expression = prompt("Espressione da tokenizzare: => ");

console.log("Token:")
console.log( toToken(expression) );