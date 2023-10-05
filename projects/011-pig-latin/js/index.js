function getPigLatin(text) {

    const wordCollection = text.match(/\w+/g); // Retur an array of only alphabetic char words.

    for (let i = 0; i < wordCollection.length; i++) {

        const notVowel = /^[^aeiou]/i; // To find if the first char is not vowel.
        const vowel = /[aeiou]/i; // To find first vowel.

        if ( wordCollection[i].match(notVowel) !== null ) {

            const vowelIndex = (wordCollection[i].search(vowel) === -1) ? 0 : wordCollection[i].search(vowel);
            
            wordCollection[i] = wordCollection[i].slice(vowelIndex) + wordCollection[i].slice(0, vowelIndex) + "ay";
        }
        else {
            wordCollection[i] += "way";
        }
    }

    return wordCollection.join(" ");
}


const prompt = require('prompt-sync')({sigint: true});

const text = prompt("Inserisci testo: => ");

console.log(getPigLatin(text));