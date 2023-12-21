
function translateToPigLatin(word) {
    const vowels = ["a", "e", "i", "o", "u"];
    let pigLatinWord = "";

    if (vowels.includes(word[0])) {
        pigLatinWord = word + "way";
    } else {
        let consonantSyllable = "";
        let i = 0;

        while (i < word.length && !vowels.includes(word[i])) {
            consonantSyllable += word[i];
             //console.log(consonantSyllable)
            i++;
        }

        //console.log(word[i])
        //console.log(word.slice(i))
        pigLatinWord = word.slice(i) + consonantSyllable + "ay";
    }

    return pigLatinWord;
}

function pigLatinTranslator(inputText) {
    const preparedStr = inputText.replace(/[^\w\s]/g, '').toLowerCase();
    const words = preparedStr.split(/\s+/);
    const translatedWords = [];

    for (let word of words) {
        translatedWords.push(translateToPigLatin(word));
    }

    return translatedWords.join(" ");
}

const userInput = prompt("insert an english sentence:");
const pigLatinResult = pigLatinTranslator(userInput);
console.log("Pig Latin: ", pigLatinResult);
