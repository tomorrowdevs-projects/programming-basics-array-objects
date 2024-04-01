'use strict';
function getTextMessaging(arrayUserMessage) {
    const arr = [];
    for (let i = 0; i < arrayUserMessage.length; i++) {
        arr.push(symbolsKeyPad[arrayUserMessage[i]]); // IPush all each elements of the array into the empty array in combination with the Keys of the object
    }

    const keyPresses = arr.toString().replaceAll(',', ''); // To replace the commas I obtain by converting the array into a string
    return keyPresses;
}

// Main programm

const userMessage = prompt(
    "Type a message to see how many times you have to press the key on your phone's keyboard to type the message text"
);
const arrayUserMessage = userMessage.split(''); //  Convert the string in an array

const symbolsKeyPad = {
    '.': 1,
    ',': 11,
    '?': 111,
    '!': 1111,
    ':': 11111,
    A: 2,
    a: 2,
    B: 22,
    b: 22,
    C: 222,
    c: 222,
    D: 3,
    d: 3,
    E: 33,
    e: 33,
    F: 333,
    f: 333,
    G: 4,
    g: 4,
    H: 44,
    h: 44,
    I: 444,
    i: 444,
    J: 5,
    j: 5,
    K: 55,
    k: 55,
    L: 555,
    l: 555,
    M: 6,
    m: 6,
    N: 66,
    n: 66,
    O: 666,
    o: 666,
    P: 7,
    p: 7,
    Q: 77,
    q: 77,
    R: 777,
    r: 777,
    S: 7777,
    s: 7777,
    T: 8,
    t: 8,
    U: 88,
    u: 88,
    V: 888,
    v: 888,
    W: 9,
    w: 9,
    X: 99,
    x: 99,
    Y: 999,
    y: 999,
    Z: 9999,
    z: 9999,
    ' ': 0,
};

const keypressesRequired = getTextMessaging(arrayUserMessage);
console.log(
    `For the user's input message "${userMessage}", the following key presses are required on the phone keypad: ${keypressesRequired} `
);
