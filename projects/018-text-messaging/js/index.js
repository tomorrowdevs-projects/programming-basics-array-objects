const prompt = require('prompt-sync')();

const arrayUserMessage = [
    ...prompt(
        "Type a message to see how many times you have to press the key on your phone's keyboard to type the message text"
    ),
];
console.log(arrayUserMessage);
// console.log(typeof arrayUserMessage);

const obj = {
    1: ['.', ',', '?', '!', ':'],
    2: ['A', 'a', 'B', 'b', 'C', 'c'],
    3: ['D', 'd', 'E', 'e', 'F', 'f'],
    4: ['G', 'g', 'H', 'h', 'I', 'i'],
    5: ['J', 'j', 'K', 'k', 'L', 'l'],
    6: ['M', 'm', 'N', 'n', 'O', 'o'],
    7: ['P', 'p', 'Q', 'q', 'R', 'r', 'S', 's'],
    8: ['T', 't', 'U', 'u', 'V', 'v'],
    9: ['W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z'],
    0: [' '],
};

// const emptyArr = [];
// const element = 'B';
const result = arrayUserMessage.map((element) => {
    for (const [key, value] of Object.entries(obj)) {
        if (value.includes(element)) {
            const index = value.indexOf(element);
            return key.toString().repeat(index + 1);
        }
    }
});
console.log(result.join(''));

// for (let i = 0; i < arrayUserMessage.length; i++) {
//     const index = value.indexOf(arrayUserMessage[i]);
//     if (value.includes(arrayUserMessage[[i]])) {
//         `${[key.repeat(index)].toString()}`;
//         if (
//             [key.repeat(index)].toString() >= 22 &&
//             [key.repeat(index)].toString() <= 99999999
//         ) {
//             console.log(`${[key.repeat(Math.ceil(index / 2))].toString()}`);
//         } else if (
//             [key.repeat(index)].toString() >= 2 &&
//             [key.repeat(index)].toString() <= 9
//         ) {
//             console.log(`${[key.repeat(index)].toString()}`);
//         } else {
//             console.log(`${[key.repeat(index)].toString()}1`);
//         }

//         emptyArr.push(key.repeat(index));
//     }
// }

// const digitMessage = emptyArr.toString().replaceAll(',', '');
// console.log(digitMessage);
