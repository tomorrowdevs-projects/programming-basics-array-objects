function getRandomNumber(min, max) {
    
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function avoidDuplicate(array, el) {
    return array.includes(el);
 }

function getLotteryNumbers(length, min, max) {
    const randomNumbers = [];

    while (randomNumbers.length < length) {
        const randomNumber = getRandomNumber(min, max);
        if(!avoidDuplicate(randomNumbers, randomNumber));
        randomNumbers.push(randomNumber);
    }
    
    return randomNumbers;
}

const numbers = getLotteryNumbers(6, 1, 49)

console.log(numbers)