'use strict';
function getScrubbleScore(userInput) {
    const scrabbleTable = {
        A: 1,
        B: 3,
        C: 3,
        D: 2,
        E: 1,
        F: 4,
        G: 2,
        H: 4,
        I: 1,
        J: 8,
        K: 5,
        L: 1,
        M: 3,
        N: 1,
        O: 1,
        P: 3,
        Q: 10,
        R: 1,
        S: 1,
        T: 1,
        U: 1,
        V: 4,
        X: 8,
        W: 4,
        Y: 4,
        Z: 10,
    };

    // Initialise a variable equal to 0 to construct the result
    let result = 0;
    const userInputArray = userInput.split('');

    for (let i = 0; i < userInputArray.length; i++) {
        result += scrabbleTable[userInputArray[i]];
    }
    return result;
}

// Main programm
const userInput = prompt(
    'Enter a word to see your Scrabble score'
).toUpperCase();

// Check user input for spaces or characters other than those required
for (let i = 0; i <= userInput.length; i++) {
    if (
        userInput.charCodeAt(i) >= 65 &&
        userInput.charCodeAt(i) <= 90 &&
        (userInput.includes(' ') === false || userInput.includes('') === false)
    ) {
        userInput;
        break;
    } else {
        console.log('Enter only one word');
        break;
    }
}

const resultScrabblePoints = getScrubbleScore(userInput);
console.log(
    `The total score for the word "${userInput}" is ${resultScrabblePoints}.`
);
