function getWords(string) {

    const wordCollection = string.split(" ");

    const symbolCollection = [",", ".", ":", ";", "-", "'", "?", "!"];

    for (let i = 0; i < wordCollection.length; i++) {

        if ( symbolCollection.includes( wordCollection[i].at(-1) ) ) {
            wordCollection[i] = wordCollection[i].split("");
            wordCollection[i].pop();
            wordCollection[i] = wordCollection[i].join("");
        }

    }

    return wordCollection;
}


const prompt = require('prompt-sync')({sigint: true});

const string = prompt("Frase: => ");

console.log(getWords(string));