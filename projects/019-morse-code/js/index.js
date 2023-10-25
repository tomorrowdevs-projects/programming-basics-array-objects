const prompt = require('prompt-sync')({sigint: true});

const message = prompt("Please enter a message: => ").toUpperCase().split(""); // Transform the user input in an array.

const morseCode = { 
// LETTERS
"A" : "._", "B" : "_...",
"C" : "_._.", "D" : "_..",	   
"E" : ".", "F" : ".._.",
"G" : "__.", "H" : "....",
"I" : "..", "J" : ".___",
"K" : "_._", "L" : "._..",
"M" : "__", "N" : "_.",
"O" : "___", "P" : ".__.",
"Q" : "__._", "R" : "._.",
"S" : "...", "T" : "_",
"U" : ".._", "V" : "..._",
"W" : ".__", "X" : "_.._",
"Y" : "_.__", "Z" : "__..",
// NUMBERS
"1" : ".____", "2" : "..___",
"3" : "...__", "4" : "...._",
"5" : ".....", "6" : "_....",
"7" : "__...", "8" : "___..",
"9" : "____.", "0" : "_____",
// ACCENTED LETTERS
"Á" : ".__._", "Ä" : "._._",
"É" : ".._..", "Ñ" : "__.__",
"Ö" : "___.", "Ü" : "..__",
}

let encodedMessage = "";
message.forEach( (letter) => { 
    
    if (Object.keys(morseCode).includes(letter))
        encodedMessage += morseCode[letter] + "  ";
});

console.log( "Your message encoded in morse code is: => " + encodedMessage);