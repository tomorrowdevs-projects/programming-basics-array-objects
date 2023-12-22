'use strict';

function getProperDivisors(positivNumber) {
    for (let num = 1; num <= positivNumber; num++) {
        if (
            positivNumber % num === 0 &&
            !isNaN(positivNumber) &&
            positivNumber !== '' &&
            positivNumber !== ' '
        ) {
            properDivisor.push(num);
        }
    }
    return properDivisor;
}

const positivNumber = Number(
    prompt(
        'Enter a positive number for which you want to find its correct divisors.'
    )
);

const properDivisor = [];

const result = getProperDivisors(positivNumber);

if (isNaN(positivNumber)) {
    console.log('Enter a valid number');
} else {
    console.log(result);
}
