function checkAnagrams(str1, str2) {

    if ( str1.length === str2.length) {
        const str1charSet = str1.split("");
        const str2charSet = str2.split("");

        const isAnagram = str1charSet.every( char => str2charSet.includes(char));
        return isAnagram;
    }

    return false;
}

const prompt = require('prompt-sync')({sigint: true});

const word1 = prompt("Enter first word: ").toUpperCase();
const word2 = prompt("Enter second word: ").toUpperCase();

console.log("The two word are anagrams? => " + checkAnagrams(word1, word2));