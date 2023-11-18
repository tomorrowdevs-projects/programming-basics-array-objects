import {createBingoCard, displayBingoCard, markBingoCard, checkWinningBingoCard} from "./bingo_functions.js";

function randomSort(array) {
    const elements = array.length;
    for (let i = elements - 1; i > 0; --i ) {
        const randomIndex = Math.floor(Math.random() * i + 1);

        [ array[randomIndex], array[i] ] = [ array[i], array[randomIndex] ]
    }
}

// Simulate games
const games = 1000; // set the games numbers
const numbersCalls = []; // create a list of numbers calls needed in every game to make a win
for (let i = 0; i < games; ++i) {

    // create the pool of numbers that can be extracted
    const poolNumbers = [];
    const endNumber = 75;
    for (let i = 1; i <= endNumber; ++i) {
    
    if (i <= 15)
    poolNumbers.push("B" + i);
    else if (i <= 30)
    poolNumbers.push("I" + i);
    else if (i <= 45)
    poolNumbers.push("N" + i);
    else if (i <= 60)
    poolNumbers.push("G" + i);
    else poolNumbers.push("O" + i);
    }

    // Sorting the numbers to prepare the game
    randomSort(poolNumbers);

    // Init a player with a BingoCard
    const player1 = createBingoCard();
    // displayBingoCard(player1);

    // Core of the game
    const totalNumbers = poolNumbers.length;
    while (totalNumbers !== 0){ // Game proceed till all the numbers are extracted

        const extractNumber = Number.parseInt(poolNumbers.pop().substring(1), 10); // Extract a sorted number from the tale of the list

        markBingoCard(player1, extractNumber); // Replace the number in the card with a 0, if there is a match

        // Check if the card is winnning
        if (checkWinningBingoCard(player1)) { // The function as side effect give the type of winning (column, row or diagonal)

            numbersCalls.push(endNumber - poolNumbers.length); // Computing how many numbers calls had done to make a win and push it to the list

            // console.log(`Winning card:`);
            // displayBingoCard(player1);
            break; // If the player won, we can exit the game
        }
    }
}

// Statistics of the games
numbersCalls.sort( (a, b) => a - b); // sort the list in ascending order

let averageCalls = 0;
numbersCalls.forEach( number => averageCalls += number);

console.log(`Average calls for ${games} games: ${averageCalls / games}\n`); // calculate the average of the calls
console.log(`Minimum calls for ${games} games: ${numbersCalls.shift()}\n`); // remove and return the first element of the list, as he correspond to the minimum
console.log(`Maximum calls for ${games} games: ${numbersCalls.pop()}\n`); // remove and return the last element of the list, as he correspond to the maximum