const prompt = require('prompt-sync')({sigint: true});

const string = prompt("Frase: => ");

console.log("La frase inserita è palindroma? => " + checkPalindrome(string));


function checkPalindrome(string) {
    
    const wordCollection = getWords( string.toLowerCase() );

    let j = wordCollection.length - 1;
    const comparingLimit = Math.ceil(wordCollection.length / 2);

    for (let i = 0; i <= comparingLimit; i++, j--) {

        if (wordCollection[i] !== wordCollection[j]) {
            return false;
        }
    }

    return true;
}

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