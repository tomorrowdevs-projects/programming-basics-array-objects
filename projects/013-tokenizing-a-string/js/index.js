'use strict';

function getTokenizeString(str) {
    for (let i = 0; i <= str.length; i++) {
        // Loop in the string to see if str doesn't include letters ecc.
        if (
            (str.charCodeAt(i) >= 33 && str.charCodeAt(i) <= 39) ||
            (str.charCodeAt(i) >= 58 && str.charCodeAt(i) <= 126) ||
            str.charCodeAt(i) === 44 ||
            str.charCodeAt(i) === 46
        ) {
            return 'Enter a mathematical expression';
            break;
        } else {
            return str.split(' ');
            break;
        }
    }
}

// Main programm
let str = prompt(
    'Type a mathematical expression. The only operators allowed are *, /, ˆ, - and +. The use of brackets is also allowed.'
);

const tokenizedString = getTokenizeString(str);
console.log(tokenizedString);
