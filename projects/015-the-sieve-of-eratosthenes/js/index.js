'use strict';

function getGetPrimeNumbers(num) {
    let primeNumbers = [];

    for (let i = 2; i <= num; i++) {
        let primeNumber = true;
        for (let j = 2; j < i; j++) {
            if (i % j === 0) {
                primeNumbers.push(0);
                primeNumber = false;
                break;
            }
        }
        if (primeNumber) {
            primeNumbers.push(i);
        }
    }
    return primeNumbers;
}

// Main programm
let num = Number(Math.trunc(prompt('Enter a number equal or greater than 2'))); // Math.trunc to remove decimal numbers

// User input is a number and not a letter
const arr = Number.isNaN(num)
    ? console.log(
          'Enter an integer greater than or equal to 2. No decimals, letters or punctuation'
      )
    : num.toString().split(' ');

const sieveOfErathosthenes = getGetPrimeNumbers(num);
console.log(sieveOfErathosthenes);
