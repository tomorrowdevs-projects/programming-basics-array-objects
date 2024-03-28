'use strict';

function traslationToPigLatin(str) {
    const arr = str.split(' ');
    // console.log(arr);

    const vowelsLetters = ['a', 'e', 'i', 'o', 'u'];
    const afterWordBeginnVowel = 'way';
    const afterWordBeginnConsonant = 'ay';
    const traslatedWords = [];

    arr.forEach(function (words) {
        for (let i = 0; i < words.length; i++) {
            let lettersUpFirstVowel = '';

            if (vowelsLetters.includes(words[i])) {
                lettersUpFirstVowel = words.substring(0, i);
                words = words.substring(i);
                const newWord = words.concat(
                    lettersUpFirstVowel,
                    afterWordBeginnConsonant
                );
                traslatedWords.push(newWord);
                break;
            }
        }
        if (
            words[0] === 'a' ||
            words[0] === 'e' ||
            words[0] === 'i' ||
            words[0] === 'o' ||
            words[0] === 'u'
        ) {
            const ciao = words.concat(afterWordBeginnVowel);
            traslatedWords.push(ciao);
        }
    });
    return traslatedWords.join(' ');
}

const str = prompt('Insert something').toLowerCase();

const result = traslationToPigLatin(str);
console.log(result);
