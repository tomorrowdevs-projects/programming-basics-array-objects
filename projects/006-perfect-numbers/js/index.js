function checkPerfectNumbers(number) {

    let properDivisorSum = 0;

    for (let divisor = (number - 1); divisor > 0; divisor--) {

        const properDivisor = number % divisor;

        if (properDivisor === 0) {
            properDivisorSum = divisor + properDivisorSum;
        }
    }

    if (properDivisorSum === number) return true;

    return false;
}

for (let i = 1; i <= 10000; i++) {

    if (checkPerfectNumbers(i) === true) {

        console.log(i);

    }

}