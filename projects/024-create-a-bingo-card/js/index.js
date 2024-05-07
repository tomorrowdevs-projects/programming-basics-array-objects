'use strict';

function randomNumber(min, max) {
    let randomNum = new Set();

    while (randomNum.size < 5) {
        randomNum.add(Math.floor(Math.random() * (max - min) + min));
    }

    return [...randomNum].sort((a, b) => a - b);
}

const generateBingoCard = () => {
    const bingostring = 'BINGO';
    let bingoCard = [...bingostring];
    let min = 1;
    let max = 16;
    for (let i = 0; i < 5; i++) {
        const bingoarray = randomNumber(min, max);
        bingoCard[i] = [bingoCard[i], bingoarray];
        min = max;
        max = max + 15;
    }
    return bingoCard;
};

const printBingoCard = (card) => {
    const cardtostamp = card.map((row) => [row[0], ...row[1]]);
    const cardrows = cardtostamp[0].length;
    const cardcols = cardtostamp.length;
    for (let i = 0; i < cardrows; i++) {
        let linetoprint = '';
        for (let j = 0; j < cardcols; j++) {
            const element = cardtostamp[j][i];
            linetoprint += element.toString().padStart(5, ' ');
        }
        console.log(linetoprint);
    }
};

const bcard = generateBingoCard();
printBingoCard(bcard);
