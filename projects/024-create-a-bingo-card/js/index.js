'use strict';
function randomBingoCard() {
    let letterB = Array.from({ length: 5 }, () =>
        Math.floor(Math.random() * 15 + 1)
    ); // From method to obtain an array of tandom numbers

    let emptyArrLetterB = [];

    while (emptyArrLetterB.length < 5) {
        letterB = Math.floor(Math.random() * 15 + 1);
        if (emptyArrLetterB.indexOf(letterB) === -1) {
            emptyArrLetterB.push(letterB);
        } // To eliminate duplicates and replace them with different numbers
    }

    let letterI = Array.from({ length: 5 }, () =>
        Math.floor(Math.random() * (31 - 16) + 16)
    );
    let emptyArrLetterI = [];
    while (emptyArrLetterI.length < 5) {
        letterI = Math.floor(Math.random() * (31 - 16) + 16);
        if (emptyArrLetterI.indexOf(letterI) === -1) {
            emptyArrLetterI.push(letterI);
        }
    }
    let letterN = Array.from({ length: 5 }, () =>
        Math.floor(Math.random() * (46 - 31) + 31)
    );
    let emptyArrLetterN = [];
    while (emptyArrLetterN.length < 5) {
        letterN = Math.floor(Math.random() * (46 - 31) + 31);
        if (emptyArrLetterN.indexOf(letterN) === -1) {
            emptyArrLetterN.push(letterN);
        }
    }
    let letterG = Array.from({ length: 5 }, () =>
        Math.floor(Math.random() * (61 - 46) + 46)
    );
    let emptyArrLetterG = [];
    while (emptyArrLetterG.length < 5) {
        letterG = Math.floor(Math.random() * (61 - 46) + 46);
        if (emptyArrLetterG.indexOf(letterG) === -1) {
            emptyArrLetterG.push(letterG);
        }
    }
    let letterO = Array.from({ length: 5 }, () =>
        Math.floor(Math.random() * (76 - 61) + 61)
    );
    let emptyArrLetterO = [];
    while (emptyArrLetterO.length < 5) {
        letterO = Math.floor(Math.random() * (76 - 61) + 61);
        if (emptyArrLetterO.indexOf(letterO) === -1) {
            emptyArrLetterO.push(letterO);
        }
    }
    // Sort to put all numbers in the columns of the bingo card  in ascending order
    emptyArrLetterB.sort(function (a, b) {
        return a - b;
    });
    emptyArrLetterI.sort(function (a, b) {
        return a - b;
    });
    emptyArrLetterN.sort(function (a, b) {
        return a - b;
    });
    emptyArrLetterG.sort(function (a, b) {
        return a - b;
    });
    emptyArrLetterO.sort(function (a, b) {
        return a - b;
    });

    return {
        emptyArrLetterB,
        emptyArrLetterI,
        emptyArrLetterN,
        emptyArrLetterG,
        emptyArrLetterO,
    };
}
const result = randomBingoCard();
console.log(result);

const bingoCardObject = { result };

console.log(bingoCardObject);
