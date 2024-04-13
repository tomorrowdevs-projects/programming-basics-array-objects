'use strict';
function checkAnagramms(firstStr, secondStr) {
    // // Delete spaces in the string to form a single word in both, convert to array, sort items in alphabetical order
    const firstText =
        firstStr.includes(' ') === true
            ? firstStr.replaceAll(' ', '').split('').sort()
            : firstStr.split('').sort();

    const secondText =
        secondStr.includes(' ') === true
            ? secondStr.replaceAll(' ', '').split('').sort()
            : secondStr.split('').sort();

    // Convert the two created arrays into two strings to compare
    const firstWordToAnagramm = firstText.join('');
    const secondWordToAnagramm = secondText.join('');

    // Visualisation of the result
    if (firstWordToAnagramm === secondWordToAnagramm) {
        return `The text of the first string "${firstStr}" and the text of the second string "${secondStr}" are anagramms`;
    } else {
        return `The text of the first string "${firstStr}" and the text of the second string "${secondStr}" are not anagramms`;
    }
}

let firstStr = prompt('Enter something').toLowerCase();
let secondStr = prompt('Enter something').toLowerCase();
const result = checkAnagramms(firstStr, secondStr);
console.log(result);
