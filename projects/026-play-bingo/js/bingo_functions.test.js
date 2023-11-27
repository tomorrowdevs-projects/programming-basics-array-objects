const { createBingoCard, displayBingoCard, markBingoCard, checkWinningBingoCard } = require("./bingo_functions");

describe('Testing the built functions for the bingo game', () => {

    describe('Testing createBingoCard()', () => {

        test('verifico che l\'ogetto abbia 5 array', () => {
            expect(Object.keys(createBingoCard())).toHaveLength(5);
        });
    
        test("verifico che l\'ogetto abbia 5 array ognuno di 5 numeri", () => {
            const object = createBingoCard();
    
            for (row in object) {
                console.log(object[row]);
                expect(object[row].length).toBe(5);
            };
        });
    });

    describe('Testing markBingoCard', () => {

        test("verifico che la funzione non ritorni niente", () => {
            const object = createBingoCard();
    
            expect(typeof displayBingoCard(object)).toBe("undefined");
        });
    
        test('testing that markBingoCard() doesn\'t change the object in place when 0, decimal, negative or strign value is passed in', () => {
            const bingoCard = createBingoCard();
            markBingoCard(bingoCard, "a"); // play with the second parameter, passing different arguments
    
            // testing that all the numbers in the card are still positive integers
            for (key in bingoCard) {
    
                bingoCard[key].forEach( number => {
                    expect(number > 0).toBe(true);
                });
            }
    
            console.log(bingoCard);
        });
    
        test('testing markBingoCard() to change the card object in place by reference', () => {
            const bingoCard = createBingoCard();
    
            expect(Object.is(createBingoCard(), markBingoCard(bingoCard, 0))).toBe(false); // two different object in the heap memory
        });
    });

    describe('Validating checkWinningBingoCard()', () => {
        
        test('simulating a row win', () => {
            const bingoCard = {
                B: [ 1, 0, 14, 10, 11 ],
                I: [ 23, 0, 29, 25, 22 ],
                N: [ 35, 0, 41, 44, 31 ],
                G: [ 49, 0, 58, 56, 48 ],
                O: [ 64, 0, 69, 72, 63 ]
            };
            
            expect(checkWinningBingoCard(bingoCard)).toBe(true);
        });

        test('call the function with no parameter throw an error', () => {
            expect(() => checkWinningBingoCard()).toThrow(); 
        });

        test('call the function with wrong parameters return false', () => {
            const fakeCard = {
                B: [ 1, 0, 14, 10, 11 ],
                I: [ 23, 0, 29, 25, 22 ],
                N: [ 35, 0, 41, 44, 31 ],
                G: [ 49, 0, 58, 56, 48 ],
                o: [ 64, 0, 69, 72, 63 ]
            };

            expect(checkWinningBingoCard("a")).toBe(false);
            expect(checkWinningBingoCard(fakeCard)).toBe(false);
        });

        test('call the function with unwinning cards return false', () => {
            const fakeCard2 = {
                B: [ 1, 0, 14, 10, 11 ],
                I: [ 23, 0, 29, 0, 22 ],
                N: [ 35, 0, 0, 44, 31 ],
                G: [ 49, 0, 58, 56, 48 ],
                O: [ 0, 60, 69, 72, 63 ]
            };
    
            const fakeCard3 = {
                B: [ 1, 0, 14, 10, 11 ],
                I: [ 23, 0, 29, 0, 22 ],
                N: [ 35, 0, 0, 44, 31 ],
                G: [ 49, 0, 58, 0, 48 ],
                O: [ 0, 60, 69, 72, 0 ]
            };
    
            expect(checkWinningBingoCard(fakeCard2)).toBe(false);
            expect(checkWinningBingoCard(fakeCard3)).toBe(false);
        });
    });
    
});