function createBingoCard() {
    const bingoCard = {};

    const bingoColumns = ["B", "I", "N", "G", "O"];

    const max = 15;
    let min = 1;

    bingoColumns.forEach( bingoColumn => {
        const bingoValues = [];

        for (let i = 0; i < 5; i++) {
            const randomNumber = Math.floor(Math.random() * max + min);

            if (!bingoValues.includes(randomNumber)) {
                bingoValues.push(randomNumber);
                continue;
            }

            i--;

        }

        bingoCard[bingoColumn] = bingoValues;

        min += 15;
    });

    return bingoCard;
}

function displayBingoCard(bingoCard) {
    let bingoLabes = "";

    for (key in bingoCard) {
        bingoLabes += key + "  | ";
    }

    let bingoRows = "";

    for (i = 0; i < 5; i++) {

        for (key in bingoCard) {
            bingoRows += bingoCard[key][i] + " | ";
        }

        bingoRows += "\n";
    }

    return `${bingoLabes}\n${bingoRows}`;
}

function markBingoCard(bingoCard) {
    
    for (i = 0; i < 5; i++) {
        
        for (key in bingoCard) {
            
            if (extractedNumbers.includes(bingoCard[key][i])) {
                bingoCard[key][i] = 0;
            }
        }
    }
}

function checkWinningBingoCard(bingoCard) {
    
    // Case 1 - All numbers in the column are marked
    for (key in bingoCard) {

        const winningColumn = bingoCard[key].every( number => {
            return number === 0;
        })

        if (winningColumn) {
            console.log("Column win");
            return true;
        }

    }

    // Case 2 - All numbers in a row are marked
    for (let i = 0; i < 5; i++) {
        let winningRow = 0;

        for (key in bingoCard) {

            if (bingoCard[key][i] === 0) {
                winningRow++;
            }
        }

        if (winningRow === 5) {
            console.log("Row win");
            return true
        }
    }

    // Case 3 - Diagonal are marked
    if (bingoCard["N"][2] === 0) {

        if ( (bingoCard["G"][1] === 0 && bingoCard["I"][3] === 0) && (bingoCard["B"][4] === 0 && bingoCard["O"][0] === 0) ) {
            
            console.log("Diagonal win");
            return true;
        }
        else if ( (bingoCard["B"][0] === 0 && bingoCard["O"][4] === 0) && (bingoCard["G"][3] === 0 && bingoCard["I"][1] === 0) ) {

            console.log("Diagonal");
            return true;
        }
    }

    return false;
}

// Tis part of code let me to create different players with one Bingo Card for once.
const ingameBingoCard = {};

for (let i = 0; i < 100; i++) { // The condition let me to control the number of players.
    ingameBingoCard[`Player${i + 1}`] = createBingoCard(); // This function create a Bingo Card object as value of the Players key.
}

// console.log(ingameBingoCard);

const disBingoCard = []; // A list to collect all the bingo cards in game.

for (key in ingameBingoCard) {
    disBingoCard.push(`${key}\n${displayBingoCard(ingameBingoCard[key])}`); // This function return the Bingo Card as styled strings.
}

console.log(`Ingame Bingo Cards:\n${disBingoCard.join("\n")}`);

// The main part of program that simulate the flow of the game
const extractedNumbers = []; // Here I collect the extracted number, which will be used inside the markBingoCard().

for(let i = 0; i < 75; i++) { // In the game there are 75 number extraction max.
    const randomNumber = Math.floor(Math.random() * 75 + 1); // Number goes from 1 to 75.

    if (!extractedNumbers.includes(randomNumber)) { // Extract the number and avoiding duplicates.
        extractedNumbers.push(randomNumber);

        for (key in ingameBingoCard) {
            markBingoCard(ingameBingoCard[key]); // By refernce, the function mark the extracted number on the Bingo Cards, if there is.
        }

        if (extractedNumbers.length >= 5) { // Only when at least 5 numbers are extracted, we check if one or more player won.
            const winningBingoCards = []; // A list to collect the winning Bungo Cards and the name of the player that own it.

            for (player in ingameBingoCard) {
                const winningBingoCard = (checkWinningBingoCard(ingameBingoCard[player])); // The function return a Boolean value. In this way we check after every additional extraction. Also, as side effect, the function display which of the 3 winning possibilities happened.

                if(winningBingoCard) {
                    winningBingoCards.push(`${player}\n${displayBingoCard(ingameBingoCard[player])}`); // Add to the list the name of the player who won the game and his string Bingo Card.
                }
            }

            if (winningBingoCards.length !== 0) { // Only if the list is empty, we can continue to extract numbers.
                console.log(`The winning cards are:\n${winningBingoCards.join("\n")}`); // Display the list the name of the player who won the game and his string Bingo Card.

                console.log(`To win we have extracted ${i} numbers.`);
                break; // One or more players won the game, so we can stop.         
            }
            
        }

        continue; // Continue here, allow to follow the normal for loop flow if no duplicated number is extracted.
    }

    i--; // When a duplicate number occours, we discard it and re-do the extraction.
}

console.log(`Extracted number list:\n${extractedNumbers.join("; ")}`);