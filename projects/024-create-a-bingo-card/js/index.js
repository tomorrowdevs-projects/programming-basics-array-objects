'use strict';
const prompt = require('prompt-sync')();

const randomNum = (min, max) => {
    const randomNumber = new Set();
    while (randomNumber.size < 5) {
        randomNumber.add(Math.floor(Math.random() * (max - min) + min));
    }
    return [...randomNumber].sort((a, b) => a - b);
};

//

const bingoCard = {
    B: randomNum(1, 15),
    I: randomNum(16, 30),
    N: randomNum(31, 45),
    G: randomNum(46, 60),
    O: randomNum(61, 75),
};

const printBingoCard = (card) => {
    const rowWithLetters = Object.keys(card).join('  ');
    console.log(rowWithLetters);

    for (let i = 0; i < 5; i++) {
        let numberBingoCard = '';

        for (let key of Object.keys(card)) {
            numberBingoCard += card[key][i].toString().padStart(2, ' ') + ' ';
        }
        console.log(numberBingoCard.trim());
    }
};
printBingoCard(bingoCard);
