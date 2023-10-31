const prompt = require('prompt-sync')({sigint: true});

function calcScrabbleScore(word) {

    const scrabblePoints = {
        1 : ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"] ,
        2 : ["D", "G"] ,
        3 : ["B", "C", "M", "P"],
        4 : ["F", "H", "V", "W", "Y"],
        5 : ["K"], 
        8 : ["J", "X"],
        10 : ["Q", "Z"],
    }

    let score = 0;
    word.split("").forEach(char => {

        let point;
        for (key in scrabblePoints) {
            if (scrabblePoints[key].includes(char)) {
                point = Number.parseInt(key, 10);
            }
        }

        score += point;
    });

    return score;
}

const scrabbleWord = prompt("Enter scrabble word: => ").toUpperCase();

console.log(`Your score is: => ${calcScrabbleScore(scrabbleWord)}`);