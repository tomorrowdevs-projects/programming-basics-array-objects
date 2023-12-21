'use strict';
let integers = [];

let insertedInteger = true;

while (insertedInteger) {
    let inputNumber = prompt('Enter a integer or digit 0 to go out');

    if (inputNumber === '0') {
        insertedInteger = false;
    } else {
        let num = parseInt(inputNumber, 10); // To convert the string in a number with base 10

        if (!isNaN(num)) {
            integers.push(num);
        } else {
            console.log('Enter a valid integer');
        }
    }
}

console.log(integers);
integers.reverse();
console.log(integers);
