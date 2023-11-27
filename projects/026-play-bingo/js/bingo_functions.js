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

    for (const key in bingoCard) {
        bingoLabes += key + "  | ";
    }

    let bingoRows = "";

    for (let i = 0; i < 5; i++) {

        for (const key in bingoCard) {
            bingoRows += bingoCard[key][i].toString().padStart(2, "0") + " | ";
        }

        bingoRows += "\n";
    }

    console.log( `${bingoLabes}\n${bingoRows}` );
}

function markBingoCard(bingoCard, extractNumber) {

    for (const key in bingoCard) {
            
        const index = bingoCard[key].indexOf(extractNumber); // check if the extract number exist inside the card object
        if (index !== -1) {
            bingoCard[key][index] = 0;
        }
    }
    
    return bingoCard;
}

function checkWinningBingoCard(bingoCard) {
    const check = Object.keys(bingoCard).every( (key, index) => {
        const columns = ["B", "I", "N", "G", "O"];
    
        return key === columns[index];
    });
    
    if (check) {
        // Case 1 - All numbers in the column are marked
        for (const key in bingoCard) {

            const winningColumn = bingoCard[key].every( number => {
                return number === 0;
            })

            if (winningColumn) {
                // console.log("Column win");
                return true;
            }

        }

        // Case 2 - All numbers in a row are marked
        for (let i = 0; i < 5; i++) {
            let winningRow = 0;

            for (const key in bingoCard) {

                if (bingoCard[key][i] === 0) {
                    winningRow++;
                }
            }

            if (winningRow === 5) {
                // console.log("Row win");
                return true
            }
        }

        // Case 3 - Diagonal are marked
        if (bingoCard["N"][2] === 0) {

            if ( (bingoCard["G"][1] === 0 && bingoCard["I"][3] === 0) && (bingoCard["B"][4] === 0 && bingoCard["O"][0] === 0) ) {
                
                // console.log("Diagonal win");
                return true;
            }
            else if ( (bingoCard["B"][0] === 0 && bingoCard["O"][4] === 0) && (bingoCard["G"][3] === 0 && bingoCard["I"][1] === 0) ) {

                // console.log("Diagonal");
                return true;
            }
        }
    }

    return false;
}

module.exports = {createBingoCard, displayBingoCard, markBingoCard, checkWinningBingoCard};