'use strict';

// Function to calculate the minimum and maximum of certain random numbers
const randomLotteryNumbers = (min, max) => {
    const randomNumber = new Set();

    while (randomNumber.size < 6) {
        randomNumber.add(Math.floor(Math.random() * (max - min) + min));
    }
    return [...randomNumber].sort((a, b) => a - b);
};

const lotteryNumbers = randomLotteryNumbers(1, 49);
const ticketNumbers = randomLotteryNumbers(1, 49);

// Comparing the numbers of the two arrays
const compareTickets = (lotteryNumbers, ticketNumbers) => {
    return JSON.stringify(lotteryNumbers) === JSON.stringify(ticketNumbers);
};

// Ternary operator to check whether the ticket is a winning one
const checkTickets = compareTickets(lotteryNumbers, ticketNumbers)
    ? console.log(
          `Your ticket numbers are ${lotteryNumbers}; 
          The numbers drawn in the lottery are: ${ticketNumbers}. 
          Therefore your ticket is a winner.`
      )
    : console.log(
          `Your ticket numbers are ${lotteryNumbers}; 
          The numbers drawn in the lottery are: ${ticketNumbers}. 
          Therefore your ticket is not a winner.`
      );
