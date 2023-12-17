function properDivisors(n) {
    // Array for to store the divisors
    let divisors = [];

    // First funct for to include just prime numbers
    function isPrime(num) {
        for (let i = 2; i < num; i++) {
            if (num % i === 0) {
                return false;
            }
        }
        // return just prime numbers, excluding 1
        return num > 1;
    }

    // iteration for to verify the divisors, from prime numbers
    for (let i = 1; i <= n; i++) {
        if (n % i === 0 && isPrime(i)) {
            divisors.push(i);
        }
    }

    return divisors;
}

const main = () => {

    const userInput = parseInt(prompt('Enter a positive integer and find out their proper divisors: '));

    // control if input is right, not negative numbers or NaN
    if (isNaN(userInput) || userInput <= 0) {
        console.log('Please enter a valid positive integer.');
    } else {
        // init properDivisions function
        const result = properDivisors(userInput);
        console.log(`Prime divisors of ${userInput}: ${result.join(', ')}`);
    }
}

//init main function
main();