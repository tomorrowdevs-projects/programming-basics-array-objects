import { removeExtremities } from './removeExtremities.js';

function main() {
    let numberList = [];
    let validInput = false;

    do {
        try {
            // List of numbers from user
            numberList = prompt("Insert a list of number, separated with space: ")
            .split(' ')
            .map(numString => parseInt(numString, 10));

            if (numberList.length >= 6 && !numberList.some(isNaN)) {
                validInput = true;
            } else {
                throw new Error("Insert at least 6 valid numbers");
            }

        } catch (error) {
            console.error(error.message);
        }

    } while (!validInput);

    try {
        // control if there are negative numbers
        if (numberList.some(num => num < 0)) {
            throw new Error("The list doesnt contain negative numbers");
        }

        // Specify the number of values to remove
        let valuesToRemove = 2;

        // Call the function for to remove the extremes
        let listWithoutExtr = removeExtremities(numberList, valuesToRemove);

        // Display the two lists, without extremes and the original 
        console.log("List without extremes:", listWithoutExtr);
        console.log("Original list:", numberList);

    } catch (error) {
        console.error(error.message);
    }

}

// Main function init
main();