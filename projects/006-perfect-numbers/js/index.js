function isPerfectNumber(n) {
    let divisors = [];

    for (let i = 1;  i <= Math.floor(n / 2); i++) {
        if (n % i === 0) {
            divisors.push(i);
        }
    }

    const perfectNumber = divisors.reduce((sum, current) => sum + current, 0);

    if (perfectNumber === n) {
       return true; 
    }

    return false;

}

function perfectNumbers() {
    const listPerfectNumbers = [];

    for (let i = 1; i <= 10000; i++) {
        if (isPerfectNumber(i)) {
            listPerfectNumbers.push(i);
        }
        
    }

    return listPerfectNumbers;

}

function main() {
    
    const userQuestion = parseInt(prompt('find out if your number is perfect: '))
    if (isNaN(userQuestion) || userQuestion <= 0) {
        console.log('Please enter a valid positive integer.');
    } else {
        if (isPerfectNumber(userQuestion)) {
            console.log(`the number ${userQuestion} is perfect`);
        } else {
            console.log(`the number ${userQuestion} is not perfect`);
        }
    
    
        const list = perfectNumbers();
        console.log(`the perfect numbers fro 1 to 10000 are: ${list}`);
    }
}

main();
