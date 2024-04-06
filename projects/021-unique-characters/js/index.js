'use strict';

function getUniqueCharacters(userInput) {
    const setUniqueCharacters = new Set(userInput.split('')); // Only unique values are retained in the set

    return setUniqueCharacters.size;
}
const userInput = prompt(
    'Enter a message to see how many unique characters it contains'
);
const result = getUniqueCharacters(userInput);
console.log(
    `The input provided by the user has a total of ${result} unique characters.`
);
