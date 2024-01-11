function costruisciMappa() {
    const mappaPressi = {
      '1': ['.', ',', '?', '!', ':'],
      '2': ['A', 'B', 'C'],
      '3': ['D', 'E', 'F'],
      '4': ['G', 'H', 'I'],
      '5': ['J', 'K', 'L'],
      '6': ['M', 'N', 'O'],
      '7': ['P', 'Q', 'R', 'S'],
      '8': ['T', 'U', 'V'],
      '9': ['W', 'X', 'Y', 'Z'],
      '0': [' ']
    };
    return mappaPressi;
}
  
function ottieniPressi(mappaPressi, messaggio) {
    let pressiNecessari = '';
  
    for (let i = 0; i < messaggio.length; i++) {
      const carattere = messaggio[i].toUpperCase();
      for (const [tasto, simboli] of Object.entries(mappaPressi)) {
        if (simboli.includes(carattere)) {
          const posizione = simboli.indexOf(carattere) + 1;
          pressiNecessari += tasto.repeat(posizione);
        }
      }
    }
  
    return pressiNecessari;
}
  
function main() {
    const mappaPressi = costruisciMappa();
  
    const messaggioUtente = prompt("Inserisci il tuo messaggio:");
    const messaggioConPressi = ottieniPressi(mappaPressi, messaggioUtente);
  
    console.log("Pressi necessari:", messaggioConPressi);
}
  
main();
  