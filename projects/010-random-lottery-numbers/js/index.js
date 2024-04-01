'use strict';

let numbersLottery = [];

while (numbersLottery.length < 6) {
    if (true) {
        let randomNumber = Math.trunc(Math.random() * 49 + 1);
        numbersLottery.push(randomNumber);
    } else {
        break;
    }
}

console.log(numbersLottery);

if (
    numbersLottery[0] !== numbersLottery[1] &&
    numbersLottery[0] !== numbersLottery[2] &&
    numbersLottery[0] !== numbersLottery[3] &&
    numbersLottery[0] !== numbersLottery[4] &&
    numbersLottery[0] !== numbersLottery[5] &&
    numbersLottery[1] !== numbersLottery[0] &&
    numbersLottery[1] !== numbersLottery[2] &&
    numbersLottery[1] !== numbersLottery[3] &&
    numbersLottery[1] !== numbersLottery[4] &&
    numbersLottery[1] !== numbersLottery[5] &&
    numbersLottery[2] !== numbersLottery[0] &&
    numbersLottery[2] !== numbersLottery[1] &&
    numbersLottery[2] !== numbersLottery[3] &&
    numbersLottery[2] !== numbersLottery[4] &&
    numbersLottery[2] !== numbersLottery[5] &&
    numbersLottery[3] !== numbersLottery[0] &&
    numbersLottery[3] !== numbersLottery[1] &&
    numbersLottery[3] !== numbersLottery[2] &&
    numbersLottery[3] !== numbersLottery[4] &&
    numbersLottery[3] !== numbersLottery[5] &&
    numbersLottery[4] !== numbersLottery[0] &&
    numbersLottery[4] !== numbersLottery[1] &&
    numbersLottery[4] !== numbersLottery[2] &&
    numbersLottery[4] !== numbersLottery[3] &&
    numbersLottery[4] !== numbersLottery[5] &&
    numbersLottery[5] !== numbersLottery[0] &&
    numbersLottery[5] !== numbersLottery[1] &&
    numbersLottery[5] !== numbersLottery[2] &&
    numbersLottery[5] !== numbersLottery[3] &&
    numbersLottery[5] !== numbersLottery[4]
) {
    const sortednumbersLottery = numbersLottery.sort((a, b) => a - b);
    console.log(sortednumbersLottery);
} else {
    console.log('Operation not valid');
}
