function createDeck() {
    const cardValue = [2, 3, 4, 5, 6, 7, 8, 9, 
                      "T", "J", "Q", "K", "A"];

    const cardSuit = ["s", "h", "d", "c"];
    
    const cardDeck = cardValue.flatMap( (value) => cardSuit.map( (suit) => value + suit ) );

    return cardDeck;
}

function shuffleDeck(cardDeck) {
    const shuffleCardDeck = [];

    while (shuffleCardDeck.length !== 52) {
        const randomIndex = Math.floor( Math.random() * 52 );

        if ( !shuffleCardDeck.includes( cardDeck[randomIndex] ) ) {
            shuffleCardDeck.push(cardDeck[randomIndex]);
        }

    }

    return shuffleCardDeck;
}


const prompt = require('prompt-sync')({sigint: true});

console.log("Mazzo di carte:");
console.log( createDeck() );

let shuffle;
do {
    console.log("Mazzo di carte mescolato:");
    console.log(shuffleDeck( createDeck() ));

    while (true) {
        shuffle = prompt("Vuoi mescolarlo nuovamente? [Si/No] => ").toLowerCase();

        if (shuffle === "si" || shuffle === "no") {
            break;
        }
        else {
            console.log("Risponidi correttamente.");
        }
    }

} while (shuffle !== "no");