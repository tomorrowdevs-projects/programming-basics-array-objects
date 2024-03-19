'use strict';

let str = prompt('Enter what do you want');

const replaceStr =
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
    str.includes(';') ||
    str.includes(' ')
        ? str
              .replace(/[,-.?!:;']/g, '')
              .toLowerCase()
              .split(' ')
        : str.split(' ');

console.log(replaceStr);

// const arr = replaceStr.reverse();

// console.log(arr);

const arr2 = replaceStr.slice().reverse();

console.log(arr2);

for (let i = 0; i < replaceStr.length; i++) {
    if (replaceStr[i] !== arr2[i]) {
        console.log('It is not palindrome');
        break;
    } else {
        console.log('It is palindrome');
    }
}
