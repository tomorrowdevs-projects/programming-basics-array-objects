function deleteDuplicates(array) {

    const newArray = [];

    for (const item of array) {

        if ( !newArray.includes(item) ) {
            newArray.push(item);
        }
    }

    return newArray;
}


const prompt = require('prompt-sync')({sigint: true});

const wordsCollection = [];

for (let i = 0, word; ; i++) {

    word = prompt("Parola: => ");

    if (word === "") {
        break;
    }

    wordsCollection[i] = word;  
}

for ( const word of deleteDuplicates(wordsCollection) ) {
        console.log(word);
}