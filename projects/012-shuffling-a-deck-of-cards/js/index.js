'use strict';
const prompt = require('prompt-sync')();

const cardDeckValues = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K'];
const cardDeckSuits = ['s', 'h', 'd', 'c'];
const sortedCardDeck = [];
const shuffledDeck = [];

// Function to create a pack of cards in order
const createDeck = () => {
    cardDeckValues.forEach((element) => {
        cardDeckSuits.forEach((i) => {
            sortedCardDeck.push(`${element}${i}`);
        });
    });
    return sortedCardDeck;
};

// Function to create a randomised pack of cards
const shuffle = () => {
    sortedCardDeck.forEach(() => {
        const randomCard = Math.floor(Math.random() * sortedCardDeck.length);
        shuffledDeck.push(sortedCardDeck[randomCard]);
    });
    return shuffledDeck;
};

const createdDeck = createDeck();
console.log(createdDeck);
const shuffledDeckCard = shuffle();
console.log(shuffledDeckCard);
