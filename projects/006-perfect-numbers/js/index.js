'use strict';

function checkPerfectNumber(num) {
    const perfectNumber = [];

    for (let i = 1; i <= num; i++) {
        if (num % i === 0) {
            perfectNumber.push(i);
        }
    }
    perfectNumber.pop(); // Remove the last element because it cannot be included in the sum of the proper divisors

    const divisors = perfectNumber.reduce(function (sum, current) {
        // To sum all elements of the array
        return sum + current;
    }, 0);

    if (divisors === num) {
        return true;
    } else {
        return false;
    }
}

const num = Number(prompt('Enter a positiv number'));

for (let j = 1; j <= 10000; j++) {
    if (checkPerfectNumber(j)) {
        console.log(`${j} is a perfect number`);
    }
}

const result = checkPerfectNumber(num);
console.log(result);
