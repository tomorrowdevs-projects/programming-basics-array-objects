'use strict';

// Function to obtain the sum of two dice
function getTwoDice() {
    const firstDice = Math.floor(Math.random() * 6 + 1);
    const secondDice = Math.floor(Math.random() * 6 + 1);
    return firstDice + secondDice;
}

const totalDiceResult = [];
const sortedTotalDiceResults = {}; // To order the results
const totalDicesRolls = 1000;

for (let i = 1; i <= totalDicesRolls; i++) {
    const diceResult = getTwoDice();

    totalDiceResult.push(getTwoDice());
    totalDiceResult.sort(function (a, b) {
        return a - b;
    });
}

console.log(totalDiceResult);

// Calculates and stores the frequency of results
for (const num of totalDiceResult) {
    sortedTotalDiceResults[num] = sortedTotalDiceResults[num]
        ? sortedTotalDiceResults[`${num}`] + 1
        : 1;
}

console.log(sortedTotalDiceResults);

const changeNameProprietyObject = {
    2: 'Number_of_times_result_two',
    3: 'Number_of_times_result_three',
    4: 'Number_of_times_result_four',
    5: 'Number_of_times_result_five',
    6: 'Number_of_times_result_six',
    7: 'Number_of_times_result_seven',
    8: 'Number_of_times_result_eight',
    9: 'Number_of_times_result_nine',
    10: 'Number_of_times_result_ten',
    11: 'Number_of_times_result_eleven',
    12: 'Number_of_times_result_twelve',
};

// Object for mapping results sorted in letters
const sortedTotalDiceResultsInLetter = {};

for (let key in sortedTotalDiceResults) {
    if (sortedTotalDiceResults.hasOwnProperty(key)) {
        let newPropertyInLetter = changeNameProprietyObject[key];
        sortedTotalDiceResultsInLetter[newPropertyInLetter] =
            sortedTotalDiceResults[key];
    }
}

console.log(sortedTotalDiceResultsInLetter);

const statisticresults = {
    Frequency_Percentage: {
        Total_two: `${
            (sortedTotalDiceResultsInLetter.Number_of_times_result_two * 100) /
            1000
        }0% frequency`,
        Total_three: `${
            (sortedTotalDiceResultsInLetter.Number_of_times_result_three *
                100) /
            1000
        }0% frequency`,
        Total_four: `${
            (sortedTotalDiceResultsInLetter.Number_of_times_result_four * 100) /
            1000
        }0% frequency`,
        Total_five: `${
            (sortedTotalDiceResultsInLetter.Number_of_times_result_five * 100) /
            1000
        }0% frequency`,
        Total_six: `${
            (sortedTotalDiceResultsInLetter.Number_of_times_result_six * 100) /
            1000
        }0% frequency`,
        Total_seven: `${
            (sortedTotalDiceResultsInLetter.Number_of_times_result_seven *
                100) /
            1000
        }0% frequency`,
        Total_eight: `${
            (sortedTotalDiceResultsInLetter.Number_of_times_result_eight *
                100) /
            1000
        }0% frequency`,
        Total_nine: `${
            (sortedTotalDiceResultsInLetter.Number_of_times_result_nine * 100) /
            1000
        }0% frequency`,
        Total_ten: `${
            (sortedTotalDiceResultsInLetter.Number_of_times_result_ten * 100) /
            1000
        }0% frequency`,
        Total_eleven: `${
            (sortedTotalDiceResultsInLetter.Number_of_times_result_eleven *
                100) /
            1000
        }0% frequency`,
        Total_twelve: `${
            (sortedTotalDiceResultsInLetter.Number_of_times_result_twelve *
                100) /
            1000
        }0% frequency`,
    },
    Probability: {
        Probability_Percentage: `For probability theory, the expected percentage for each total is equal to: ${(
            1000 / 110
        ).toFixed(2)}%`,
    },
};

console.log(statisticresults.Frequency_Percentage);
console.log(statisticresults.Probability);
