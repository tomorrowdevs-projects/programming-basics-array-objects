'use strict';
const prompt = require('prompt-sync')();
const printBingoCard = require('../../024-create-a-bingo-card/js/index');
// import { printBingoCard } from '../../024-create-a-bingo-card/js';

/**
 * The function takes 2 different numbers and returns an ordered array of 5 numbers without duplicates.
 * @param {number} min - The minimum value to generate the random number.
 * @param {number} max - The maximum value to generate the random number.
 * @returns {number[]} An ordered array of 5 random numbers
 */
const randomNum = (min, max) => {
    const randomNumber = new Set();
    while (randomNumber.size < 5) {
        randomNumber.add(Math.floor(Math.random() * (max - min) + min));
    }
    return [...randomNumber].sort((a, b) => a - b);
};

/**
 * The function generates a minimum and maximum number.
 * @param {number} min - The minimum value
 * @param {number} max - The maximum value
 * @returns {number}  A random number between min and max
 */
const getBingoNumber = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
};

// Generate Bingo Card
const bingoCard = {
    B: randomNum(1, 15),
    I: randomNum(16, 30),
    N: randomNum(31, 45),
    G: randomNum(46, 60),
    O: randomNum(61, 75),
};
// Dichiarazione di funzione - parametro

// printBingoCard(); // Chiamata della funzione - (Argomento)
const extractedNumbers = [];
let winningLineMessage = '';

do {
    const randomBingoNumber = getBingoNumber(1, 75);

    if (!extractedNumbers.includes(randomBingoNumber)) {
        extractedNumbers.push(randomBingoNumber);
        for (const key in bingoCard) {
            if (bingoCard[key].includes(randomBingoNumber)) {
                const index = bingoCard[key].indexOf(randomBingoNumber);
                bingoCard[key][index] = 0;
            }
        }
    }

    // To print the winning line
    if (!winningLineMessage && isWinnerHorizontalLine(bingoCard)) {
        winningLineMessage =
            'The winning line on your bingo card is the horizontal line';
        break;
    } else if (!winningLineMessage && isWinnerVerticalLine(bingoCard)) {
        winningLineMessage =
            'The winning line on your bingo card is the vertical line';
        break;
    } else if (!winningLineMessage && isWinnerDiagonalLine(bingoCard)) {
        winningLineMessage =
            'The winning line on your bingo card is the diagonal line';
        break;
    }
} while (
    !isWinnerHorizontalLine(bingoCard) ||
    !isWinnerVerticalLine(bingoCard) ||
    !isWinnerDiagonalLine(bingoCard)
);

console.log(bingoCard);
console.log(winningLineMessage);
// Card in questo è un oggetto

/**
 * Check if there is a winning horizontal line on the bingo card
 * @param {object} card - The bingo card.
 * @returns {boolean} True if there is a winning horizontal line, false otherwise.
 */
function isWinnerHorizontalLine(card) {
    for (const key in card) {
        if (card[key].reduce((a, b) => a + b) === 0) {
            return true;
        }
    }
    return false;
}

/**
 * Check if there is a winning vertical line on the bingo card.
 * @param {object} card - The bingo card.
 * @returns {boolean} - True if there is a winning horizontal line, false otherwise
 */
function isWinnerVerticalLine(card) {
    const indexMax = card[Object.keys(card)[0]].length;

    for (let i = 0; i < indexMax; i++) {
        const emptyArr = [];
        for (const key in card) {
            emptyArr.push(card[key][i]);
        }
        if (emptyArr.reduce((a, b) => a + b) === 0) {
            return true;
        }
    }
    return false;
}

/**
 * Check if there is a winning diagonal line on the bingo card.
 * @param {object} card - The bingo card.
 * @returns  {boolean} - True if there is a winning diagonal line, false otherwise
 */
function isWinnerDiagonalLine(card) {
    const indexMax = card[Object.keys(card)[0]].length;
    let diagonaltoRightSum = 0;
    let diagonaltoLeftSum = 0;

    for (let i = 0; i < indexMax; i++) {
        if (card[Object.keys(card)[i]][i] !== 0) {
            diagonaltoRightSum = false;
        }
        if (card[Object.keys(card)[indexMax - i - 1]][i] !== 0) {
            diagonaltoLeftSum = false;
        }
    }
    return diagonaltoLeftSum === 0 || diagonaltoRightSum === 0;
}

module.exports = isWinnerHorizontalLine;
module.exports = isWinnerVerticalLine;
module.exports = isWinnerDiagonalLine;
// sayHello();
// function sayHello() {
//     console.log('Hello World!');
// }
// Hoisting
// console.log(Object.values(bingoCard));
// console.log(typeof Object.entries(bingoCard));
// printBingoCard(bingoCard);
