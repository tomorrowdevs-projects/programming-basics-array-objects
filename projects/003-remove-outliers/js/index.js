'use strict';

function removeOutliers(listValues, nonNegativeInteger) {
    if (
        listValues.length >= 4 &&
        nonNegativeInteger > 0 &&
        (!isNaN(nonNegativeInteger) ||
            nonNegativeInteger !== '' ||
            nonNegativeInteger !== ' ')
    ) {
        let newArray = listValues.sort().concat(nonNegativeInteger2);
        // const newArray = newArray.sort();
        // console.log(newArray);

        const firstTwoItems = newArray.splice(0, 2);
        // console.log(firstTwoItems);
        const lastTwoItems = newArray.splice(-2, 2);
        // console.log(lastTwoItems);

        const excludedExtremeItems = firstTwoItems.concat(lastTwoItems);

        return [excludedExtremeItems, newArray];
    } else {
        console.log(
            'You have to enter minimum 4 values or an integer non negative'
        );
    }
}

const nonNegativeInteger = Number(prompt('Enter a non-negative integer'));

const listValues = [];

let value = true;

while (value) {
    const insertedValue = prompt(
        'Enter a list of values (e.g. city, things, etc.). Digit end to finish;'
    );
    if (
        insertedValue === 'end' &&
        (insertedValue !== '' || insertedValue !== ' ')
    ) {
        value = false;
    } else {
        listValues.push(insertedValue);
    }
}

console.log(listValues);

// Convert the number in a string
const convertednonNegativeInteger = String(nonNegativeInteger);

// After converting the number into a string, I convert the string into an array
const nonNegativeInteger2 = convertednonNegativeInteger.split();

const result = removeOutliers(listValues, nonNegativeInteger);
console.log(result);
