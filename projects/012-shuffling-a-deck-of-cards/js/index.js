'use strict';

function createDeck() {
    let deckCards = [];

    // Cycle through the individual card numbers from 1 to 52.
    for (let singleCard = 1; singleCard <= 52; singleCard++) {
        if (singleCard === 1) {
            deckCards.push('As');
        } else if (singleCard >= 2 && singleCard <= 10) {
            deckCards.push(`${singleCard}s`);
        } else if (singleCard === 11) {
            deckCards.push('Js');
        } else if (singleCard === 12) {
            deckCards.push('Qs');
        } else if (singleCard === 13) {
            deckCards.push('Ks');
        } else if (singleCard === 14) {
            deckCards.push('Ah');
        } else if (singleCard >= 15 && singleCard <= 23) {
            deckCards.push(`${singleCard - 13}h`);
        } else if (singleCard === 24) {
            deckCards.push('Jh');
        } else if (singleCard === 25) {
            deckCards.push('Qh');
        } else if (singleCard === 26) {
            deckCards.push('Kh');
        } else if (singleCard === 27) {
            deckCards.push('Ad');
        } else if (singleCard >= 28 && singleCard <= 36) {
            deckCards.push(`${singleCard - 26}d`);
        } else if (singleCard === 37) {
            deckCards.push('Jd');
        } else if (singleCard === 38) {
            deckCards.push('Qd');
        } else if (singleCard === 39) {
            deckCards.push('Kd');
        } else if (singleCard === 40) {
            deckCards.push('Ac');
        } else if (singleCard >= 41 && singleCard <= 49) {
            deckCards.push(`${singleCard - 39}c`);
        } else if (singleCard === 50) {
            deckCards.push('Jc');
        } else if (singleCard === 51) {
            deckCards.push('Qc');
        } else {
            deckCards.push('Kc');
        }
    }
    return deckCards;
}

function shuffle() {
    let checkDuplicatesCard = [];

    for (let singleCard = 1; singleCard <= 52; singleCard++) {
        let deckCards = createDeck();

        let randomCard = Math.floor(Math.random() * 52 + 1);
        let shuffleCard = deckCards[randomCard];
        checkDuplicatesCard.push(shuffleCard);
        deckCards.splice(randomCard, 1);
    }
    return checkDuplicatesCard;
}

// Main programm
const deckOfCards = createDeck();
console.log(deckOfCards);
const shuffleDeckOfCards = shuffle();
console.log(shuffleDeckOfCards);
