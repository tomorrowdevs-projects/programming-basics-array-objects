'use strict';
const prompt = require('prompt-sync')();

const printBingoCard = require('../../024-create-a-bingo-card/js/index');
const isWinnerHorizontalLine = require('../../025-checking-for-a-winning-card/js/index');
const isWinnerVerticalLine = require('../../025-checking-for-a-winning-card/js/index');
const isWinnerDiagonalLine = require('../../025-checking-for-a-winning-card/js/index');
// import { printBingoCard } from '../../024-create-a-bingo-card/js';

const emptyArray = [];

// Simulate 1000
for (let i = 1; i <= 1000; i++) {
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

    // To store in an array the extracted numbers
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

        // The number of items within the array corresponds to the number of calls required to have a winning line horizontally, vertically or diagonally
        if (!winningLineMessage && isWinnerHorizontalLine(bingoCard)) {
            winningLineMessage = extractedNumbers.length - 1;
            emptyArray.push(winningLineMessage);
            break;
        } else if (!winningLineMessage && isWinnerVerticalLine(bingoCard)) {
            winningLineMessage = extractedNumbers.length - 1;
            emptyArray.push(winningLineMessage);
            break;
        } else if (!winningLineMessage && isWinnerDiagonalLine(bingoCard)) {
            winningLineMessage = extractedNumbers.length - 1;
            emptyArray.push(winningLineMessage);
            break;
        }
    } while (
        !isWinnerHorizontalLine(bingoCard) ||
        !isWinnerVerticalLine(bingoCard) ||
        !isWinnerDiagonalLine(bingoCard)
    );
}
// console.log(emptyArray);

/**
 * The sort method for arranging numerical items within the array in ascending order
 * @param {number} a
 * @param {number} b
 * @returns An array of numbers in ascending order
 */
const sortedNumbersOfCalls = (a, b) => {
    return a - b;
};

const numberOfCalls = emptyArray.sort(sortedNumbersOfCalls);

// The first in the array of numbers arranged in ascending order represents the minimum value
const minimumNumberOfCalls = numberOfCalls.shift();

// The first in the array of numbers arranged in ascending order represents the maximum value
const maximumNumberOfCalls = numberOfCalls.pop();
const initialValue = 0;

// To calculate the average number of calls to a winning bingo card
const averageNumberOfCalls = (
    numberOfCalls.reduce(
        (accumulator, currentValue) => accumulator + currentValue,
        initialValue
    ) / 1000
).toFixed(0);

console.log(`Out of a total of 1000 games, the minimum number of calls that must be made before a bingo card is a winner is equal to: ${minimumNumberOfCalls}.
The maximum number of calls is equal to: ${maximumNumberOfCalls}
The average number of calls is equal to: ${averageNumberOfCalls}`);
