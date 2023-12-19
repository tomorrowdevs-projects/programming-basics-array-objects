function processString(inputString) {
    //replace the punctuation marks with regex, split the string in words and save in an array
    const wordsArray = inputString.replace(/[.,\/#!?$%\^&\*;:{}=\-_`~()]/g, "").split(/\s+/);
    return wordsArray.filter(word => word !== "'");
}

function main() {
    userInput = prompt('Write a sentence: ');
    const result = processString(userInput);
    console.log(result);
}

main();