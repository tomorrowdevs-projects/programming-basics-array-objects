'use strict';

function removePunctuationMarks(str) {
    if (
        str.includes(',') ||
        str.includes('-') ||
        str.includes('.') ||
        str.includes('?') ||
        str.includes('-') ||
        str.includes(" '") ||
        str.includes("' ") ||
        str.includes("'''") ||
        str.includes('!') ||
        str.includes(':') ||
        str.includes(';')
    ) {
        let arr = str.replace(/[,-.?!:;']/g, '').split(' ');
        return arr;
    } else {
        let arr = str.split(' '); // If there are no punctuation marks indicated in the text of the exercise
        return arr;
    }
}

// main programm
const str = prompt('Enter all the words that you want');
const checkPunctuationMarks = removePunctuationMarks(str);
console.log(checkPunctuationMarks);
