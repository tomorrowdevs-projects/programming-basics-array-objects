'use strict';

function getSingleWords() {
    words.forEach(function (duplicateWord) {
        if (!wordsWithoutDuplicates.includes(duplicateWord)) {
            // Check if the word is not present in this array
            wordsWithoutDuplicates.push(duplicateWord);
        }
    });

    return wordsWithoutDuplicates;
}

const words = [];

const wordsWithoutDuplicates = []; // Second array to store the words without duplicates

while (true) {
    const userWords = prompt(
        'Type a word and press Enter; type as many words as you like (press Enter with a blank line to end)'
    );

    if ((userWords === '' || userWords === ' ') && !isNaN(userWords)) {
        break;
    } else {
        words.push(userWords);
    }
}

console.log(words);

const result = getSingleWords();
console.log(result);
