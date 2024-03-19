'use strict';

function isSublist(firstList, secondList) {
    for (
        let i = 0, j = 0;
        i < firstList.length, j < secondList.length;
        i++, j++
    ) {
        // Checking if one of the 2 arrays is empty
        if (
            secondList.includes(' ') ||
            secondList.includes('') ||
            firstList.includes(' ') ||
            firstList.includes('')
        ) {
            return true;
            break;
        } else if (firstList.length >= secondList.length) {
            // Loop in the second array to check it is a Sublist
            if (firstList.indexOf(secondList[j]) === i) {
                return true;
            } else {
                return false;
                break;
            }
        } else if (firstList.length < secondList.length) {
            // Loop in the first array to check it is a Sublist
            if (secondList.indexOf(firstList[i]) === j) {
                return true;
            } else {
                return false;
                break;
            }
        }
    }
}
// Main program
const str = prompt('Digit something');
const str2 = prompt('Digit something else');
const firstList = str.split(' ');
const secondList = str2.split(' ');

const theListIsSubList = isSublist(firstList, secondList);
console.log(theListIsSubList);
