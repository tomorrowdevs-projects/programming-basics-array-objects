// CREATE MY OWN RANGE FUNCTION - IT'S MY INTERPRETATION OF HOW I THINK IT'S WORK UNDER THE HOOD IN PYTHON
function getRange(start = 0, stop, step = 1) {
    const numberCollection = [];

    for (let i = start, j = 0; i < stop; i = i + step, j++) {
        numberCollection[j] = i;
    }

    return numberCollection;
}

function isIncluded(item, index) {
    if (notPrimeNumbers.includes(item)) {
        numberCollection[index] = 0;
    }
}

// Program:

const prompt = require('prompt-sync')({sigint: true});

const baseNumber = 2;

console.log("QUESTO PROGRAMMA MOSTRA TUTTI I NUMERI PRIMI COMPRESI TRA " + baseNumber + " E IL NUMERO DESIDERATO.");
console.log("Primo numero della serie: => " + baseNumber);

const endLimit = Number( prompt("Inserisci l'ultimo numero della serie: => ") );

const numberCollection = getRange(baseNumber, endLimit);
const notPrimeNumbers = getRange(2, endLimit, 2);

numberCollection.forEach(isIncluded);

console.log("I numeri primi compresi tra 2 e " + endLimit + " sono: ");
for (number of numberCollection) {

    if (number !== 0) console.log(number);
}

// SOLUTION2 -- THI SOLUTION USE LESS CODE BUT DOESN'T RESPECT PERFECTLY THE PROCEDURE REQUIRED BY README.md FILE

// function getRange(start = 0, stop, step = 1) {
//     const numberCollection = [];

//     for (let i = start, j = 0; i < stop; i = i + step, j++) {
//         numberCollection[j] = i;
//     }

//     return numberCollection;
// }

// // Program:

// const prompt = require('prompt-sync')({sigint: true});

// const baseNumber = 9;

// console.log("QUESTO PROGRAMMA MOSTRA TUTTI I NUMERI PRIMI COMPRESI TRA " + baseNumber + " E IL NUMERO DESIDERATO.");
// console.log("Primo numero della serie: => " + baseNumber);

// const endLimit = Number( prompt("Inserisci l'ultimo numero della serie: => ") );

// const numberCollection = getRange(baseNumber, endLimit);
// const notPrimeNumbers = getRange(2, endLimit, 2);

// console.log("I numeri primi compresi tra 2 e " + endLimit + " sono: ");
// for (number of numberCollection) {

//     if (!notPrimeNumbers.includes(number)) console.log(number);
// }