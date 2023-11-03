function getBingoCard() {

    const bingoCard = {};

    const column = ["B", "I", "N", "G", "O"];
    const max = 15;
    let min = 1;

    column.forEach( letter => {
        const numberList = [];

        for (let i = 0; i < 5; i++) {
            numberList.push( Math.floor(Math.random() * max + min) );
        }

        bingoCard[letter] = numberList;

        min += 15;
    });

    return bingoCard;
};

function displayBingoCard(bingoCard) {
    
    let columnLabels = "";
    for (key in bingoCard) {
        columnLabels += key + "  | ";
    }

    let bingoRows = "";
    for (let i = 0; i < 5; i++) {

        for (key in bingoCard) {
            bingoRows += bingoCard[key][i] + " | ";
        }

        bingoRows += "\n";
    }

    return `${columnLabels}\n${bingoRows}`;
}

const bingoCard = getBingoCard();
console.log(bingoCard);
console.log(displayBingoCard(bingoCard));