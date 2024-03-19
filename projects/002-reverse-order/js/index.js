'use strict';

let numbers = [];

let insertedNumber = true;

while (insertedNumber) {
    let inputNumber = prompt('Enter a integer or digit 0 to go out');

    if (inputNumber === '0') {
        insertedNumber = false;
    } else {
        let num = parseInt(inputNumber, 10);

        if (!isNaN(num)) {
            numbers.push(num);
        } else {
            console.log('Enter a valid integer');
        }
    }
}

console.log(numbers);
let arr = numbers.reverse();
console.log(arr);
