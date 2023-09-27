const prompt = require('prompt-sync')({sigint: true});

const array = [];
for (let i = 0; true; i++) {
    const number = Number( prompt("Numero: => ") );

    if (number === 0) {
        break;
    }

    array[i] = number;
}

array.sort(function(p1, p2){return p1 - p2});

for (const number of array) {
    console.log(number);
}