function getPigLatin(text) {

    const wordCollection = text.match(/\w+/g);

    for (let i = 0; i < wordCollection[i].length; i++) {

        if ( wordCollection[i].match(/^[^aeiou]/i) !== null ) {
            wordCollection[i] = wordCollection[i].substring( wordCollection[i].search(/[aeiou]/i) ) + wordCollection[i].match(/^[^aeiou]+/i).join("") + "ay";
        }
        else {
            wordCollection[i] += "way";
        }
    }

    return wordCollection.join(" ");
}


const prompt = require('prompt-sync')({sigint: true});

const text = prompt("Inserisci testo: => ");

const pigLatinText = getPigLatin(text);

console.log(pigLatinText);