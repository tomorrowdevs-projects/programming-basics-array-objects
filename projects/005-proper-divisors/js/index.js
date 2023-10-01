const prompt = require('prompt-sync')({sigint: true});

const number = Number( prompt("Numero: ") );

showProperDivisor(number);

function showProperDivisor(number) {

  const divisorCollection = [];

  for (let divisor = (number - 1); divisor != 1; divisor--) {
    const properDivisor = number % divisor;

    if (properDivisor === 0) {
      divisorCollection.push(divisor);
    }

  }

  return console.log(divisorCollection);
  
}
