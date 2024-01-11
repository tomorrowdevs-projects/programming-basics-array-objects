function traduciInMorse(carattere) {
    const morseMapping = {
      'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
      'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
      'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
      '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
      'Á': '.-.-', 'Ä': '.-.-', 'É': '..-..', 'Ñ': '--.--', 'Ö': '---.', 'Ü': '..--'
    };
  
    return morseMapping[carattere.toUpperCase()] || '';
  }
  
  function traduciMessaggioInMorse(messaggio) {
    let morse = '';
  
    for (let i = 0; i < messaggio.length; i++) {
      const carattere = messaggio[i];
      
      if (/[A-Za-z0-9ÁÄÉÑÖÜ]/.test(carattere)) {
        const codiceMorse = traduciInMorse(carattere);
        morse += codiceMorse + ' ';
      }
    }
  
    return morse.trim();
  }
  
  const messaggioUtente = prompt("Inserisci il tuo messaggio:");
  const messaggioInMorse = traduciMessaggioInMorse(messaggioUtente);
  
  console.log("Messaggio in Morse:", messaggioInMorse);
  