function isWordByWordPalindrome(str) {
    const preparedStr = str.replace(/[^\w\s]/g, '').toLowerCase();
    const wordsArray = preparedStr.split(/\s+/);

    return wordsArray.join('') === wordsArray.reverse().join('');
}

const userInput = prompt('Insert a sentence: ');

if (isWordByWordPalindrome(userInput)) {
    console.log(userInput, ': This sentence is a palindrome');
} else {
    console.log(userInput, ': Your sentence is not a palindrome');
}
