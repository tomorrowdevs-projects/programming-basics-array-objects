'use strict';

function getListString(listofString) {
    // Search for and remove any user-entered punctuation marks
    const allItems =
        listofString.includes(',') ||
        listofString.includes('-') ||
        listofString.includes('.') ||
        listofString.includes('?') ||
        listofString.includes('-') ||
        listofString.includes(" '") ||
        listofString.includes("' ") ||
        listofString.includes("'''") ||
        listofString.includes('!') ||
        listofString.includes(':') ||
        listofString.includes(';') ||
        listofString.includes(' ')
            ? listofString.replace(/[,-.?!:;']/g, '').split(' ')
            : listofString.split(' ');

    if (allItems.length === 1) {
        allItems;
    } else if (allItems.length >= 2) {
        allItems.splice(allItems.length - 1, 0, 'and');
        allItems;
    } else {
        ('Insert something');
    }

    // Convert the array to a string
    const newStr = allItems.join(' ');
    // console.log(newStr);

    // Insert a comma between each word in the string
    const str2 =
        newStr.includes(' ') === true && allItems.length > 2 === true
            ? newStr.replaceAll(' ', ', ')
            : newStr;
    // I remove the comma before and after and
    let str3 =
        str2.includes(' and, ') === true
            ? str2.replace(', and, ', ' and ')
            : str2;

    return str3;
}

// main programm
const listofString = prompt('Enter what you desire');
const result = getListString(listofString);
console.log(result);
