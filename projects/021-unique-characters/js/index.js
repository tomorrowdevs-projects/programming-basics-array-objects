function calcUniqueCharacters(string) {
    const charCollection = string.split("");

    const charSet = new Set();

    charCollection.forEach( char => charSet.add(char));
    
    return charSet.size;
}

const prompt = require('prompt-sync')({sigint: true});

const text = prompt("Enter text: => ");

console.log("Number of unique characters: => " + calcUniqueCharacters(text));