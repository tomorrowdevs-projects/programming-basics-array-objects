// Declaration of array of numbers's user
const userNumbers = [];

// var for to memorize user's input
let userPrompt;

// Main function, for to memorize and read the numbers of the user
const numbersReader = () => {
    // cicle that continues as long as the users input isnt 0
    do {
        userPrompt = parseInt(prompt('Insert number: '));
        
        // controll if user prompt is an integer
        if (Number.isInteger(userPrompt)) {
            // store of inputs and sorting
            userNumbers.push(userPrompt);
            userNumbers.sort((a, b) => a - b);
            // log of numbers list in different lines
            console.log('your current list: ');
            userNumbers.forEach(number => console.log(number));
        } else {
            alert('It isn\'t a number.');
        }

    } while (userPrompt !== 0);
    // final message
    console.log('Your number list is: ', userNumbers);
}

// function init
numbersReader();
