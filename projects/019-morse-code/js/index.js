const prompt = require('prompt-sync')();

const inputMessage = [
    ...prompt('Enter text to see Morse translated').toUpperCase(),
];

const morseCodeDictionary = {
    A: '. -',
    B: '- . . .',
    C: '- . - .',
    D: '- . .',
    E: '.',
    F: '. . - .',
    G: '- - .',
    H: '. . . .',
    I: '. .',
    J: '. - - -',
    K: '- . -',
    L: '. - . .',
    M: '- -',
    N: '- .',
    O: '- - -',
    P: '. - - .',
    Q: '- - . -',
    R: '. - .',
    S: '. . .',
    T: '-',
    U: '. . -',
    V: '. . . -',
    W: '. - -',
    X: '- . . -',
    Y: '- . - -',
    Z: '- - . .',
    1: '. - - - -',
    2: '. . - - -',
    3: '. . . - -',
    4: '. . . . -',
    5: '. . . . .',
    6: '- . . . .',
    7: '- - . . .',
    8: '- - - . .',
    9: '- - - - .',
    10: '- - - - -',
    Á: '. - - . -',
    Ä: '. - . -',
    É: '. . - . .',
    Ñ: '- - . - -',
    Ö: '- - - .',
    Ü: '. . - -',
}; // Map characters to their corresponding Morse code
const arrCode = inputMessage.map((element) => morseCodeDictionary[element]);
console.log(arrCode);

// for (let i = 0; i < messageArray.length; i++) {
//     morseCodeArray.push(morseCodeDictionary[messageArray[i]]); // Translates each character of the text into Morse code and adds it to the Morse code array
// }

// let formattedMorseText = morseCodeArray.toString().replaceAll(',', '  ');
// console.log(formattedMorseText);
