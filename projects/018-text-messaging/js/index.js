const prompt = require('prompt-sync')({sigint: true});

const message = prompt("Please enter a message: => ").toUpperCase().split(""); // Transform the user input in an array.

const numericKeypad = { // Create an object with array as property values.
    1 : [".", ",", "?", "!", ":"],
    2 : ["A", "B", "C"],
    3 : ["D", "E", "F"],
    4 : ["G", "H", "I"],
    5 : ["J", "K", "L"],
    6 : ["M", "N", "O"],
    7 : ["P", "Q", "R", "S"],
    8 : ["T", "U", "V"],
    9 : ["W", "X", "Y", "Z"],
    0 :[" "],
}

const keypadSequence = [];

message.forEach( (letter) =>  {

    for (let numericKey in numericKeypad) {
        const letterSet = numericKeypad[numericKey];

        if ( letterSet.includes(letter) ) {
            const letterSetPosition = letterSet.indexOf(letter) + 1;

            for (let i = 0; i < letterSetPosition; i++) {
                keypadSequence.push(numericKey);
            }
        }
    }
})

console.log("You pressed this sequence of digit: => " + keypadSequence.join(""));