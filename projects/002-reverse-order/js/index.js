const prompt = require('prompt-sync')({sigint: true});

const array = [];
for (let i = 0; true; i++) {
    const number = Number( prompt("Numero: => ") );

    if (number === 0) {
        break;
    }

    array[i] = number;
}

array.reverse();

for (const number of array) {
    console.log(number);
}