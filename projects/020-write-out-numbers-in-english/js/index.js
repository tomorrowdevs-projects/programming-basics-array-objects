const prompt = require('prompt-sync')({sigint: true});

const number = prompt("Enter a number: => ").split("");


function numberToWord(number) {

    const englishWordsNumbers = {
        units : {
                0 : "zero",
                1 : "one",
                2 : "two",
                3 : "three",
                4 : "four",
                5 : "five",
                6 : "six",
                7 : "seven",
                8 : "eight",
                9 : "nine",
                },
        tens : {
                10 : "ten",
                11 : "eleven",
                12 : "twelve",
                13 : "thirteen",
                14 : "fourteen",
                15 : "fifteen",
                16 : "sixteen",
                17 : "seventeen",
                18 : "eighteen",
                19 : "nineteen",
                20 : "twenty",
                30 : "thirty",
                40 : "forty",
                50 : "fifty",
                60 : "sixty",
                70 : "seventy",
                80 : "eighty",
                90 : "ninety",
                },
        hundreds : "hundred",
        }
    
        if (number.length === 3) {
            const hundredsNumber = Number( number.slice(0, 1) );
            
            if ( number.slice(1).join("") === "00") {
                return englishWordsNumbers.units[hundredsNumber] + " " + englishWordsNumbers.hundreds;
            }
            else if ( number[1] === "0") {

                return englishWordsNumbers.units[hundredsNumber] + " " + englishWordsNumbers.hundreds + " and " + numberToWord(number.pop());
            }

            number.shift();
            return englishWordsNumbers.units[hundredsNumber] + " " + englishWordsNumbers.hundreds + " " + numberToWord(number);
        }
        else if (number.length === 2) {
            const unitsNumber = Number( number.slice(1) );
            const tensNumber = Number( number.join("") );

            if ( Object.keys(englishWordsNumbers.tens).includes(tensNumber.toString()) ) {
                return englishWordsNumbers.tens[tensNumber];
            }

            return englishWordsNumbers.tens[tensNumber - unitsNumber] + " " + englishWordsNumbers.units[unitsNumber];
        }
        else if (number.length === 1) {
            return englishWordsNumbers.units[number];
        }
}

console.log("Number in English: => " + numberToWord(number));