'use strict';
function convertNumberInEnglish(userInput) {
    const numberInEnglish = {
        100: 'one hundred',
        200: 'two hundred',
        300: 'three hundred',
        400: 'four hundred',
        500: 'five hundred',
        600: 'six hundred',
        700: 'seven hundred',
        800: 'eight hundred',
        900: 'nine hundred',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    };

    let result = ''; // Initialise an empty string to construct the result
    if (userInput >= 100 && userInput % 100 >= 20) {
        let arrayNumberDivided = [
            userInput - (userInput % 100),
            (userInput % 100) - (userInput % 10),
            userInput % 10,
        ];

        for (let i = 0; i < arrayNumberDivided.length; i++) {
            result += numberInEnglish[arrayNumberDivided[i]] + ' '; // Add each element to the result
        }
    } else if (
        userInput >= 100 &&
        userInput % 100 < 20 &&
        userInput % 100 >= 10
    ) {
        let arrayNumberDivided = [
            userInput - (userInput % 100),
            userInput % 100,
        ];
        for (let i = 0; i < arrayNumberDivided.length; i++) {
            result += numberInEnglish[arrayNumberDivided[i]] + ' ';
        }
    } else if (
        userInput >= 100 &&
        userInput % 100 <= 10 &&
        userInput % 100 >= 1
    ) {
        let arrayNumberDivided = [
            userInput - (userInput % 100),
            userInput % 10,
        ];
        for (let i = 0; i < arrayNumberDivided.length; i++) {
            result += numberInEnglish[arrayNumberDivided[i]] + ' ';
        }
    } else if (userInput < 100 && userInput % 100 >= 20) {
        let arrayNumberDivided = [userInput - (userInput % 10), userInput % 10];
        for (let i = 0; i < arrayNumberDivided.length; i++) {
            result += numberInEnglish[arrayNumberDivided[i]] + ' ';
        }
    } else if (userInput >= 100 && userInput % 100 === 0) {
        let arrayNumberDivided = [userInput];
        for (let i = 0; i < arrayNumberDivided.length; i++) {
            result += numberInEnglish[arrayNumberDivided[i]] + ' ';
        }
    } else {
        let arrayNumberDivided = [userInput];
        for (let i = 0; i < arrayNumberDivided.length; i++) {
            result += numberInEnglish[arrayNumberDivided[i]] + ' ';
        }
    }
    return result.trim(); // Return the result after removing any excess blanks
}
let userNumber = prompt('Enter a number between 0 and 999');

for (let i = 0; i <= userNumber.length; i++) {
    if (
        userNumber.charCodeAt(i) >= 48 &&
        userNumber.charCodeAt(i) <= 57 &&
        userNumber.length <= 3
    ) {
        userNumber;
        break;
    } else {
        console.log('Enter a number between 0 and 999');
    }
}
let userInput = Number(userNumber);
const result = convertNumberInEnglish(userInput);
console.log(result);
