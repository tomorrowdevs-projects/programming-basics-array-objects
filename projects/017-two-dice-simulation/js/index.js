function lancioDadi() {
  const dado1 = Math.floor(Math.random() * 6) + 1;
  const dado2 = Math.floor(Math.random() * 6) + 1;
  return dado1 + dado2;
}

function simulaLanci(numLanci) {
  let frequenze = Array(11).fill(0);

  for (let i = 0; i < numLanci; i++) {
    let risultato = lancioDadi();
    frequenze[risultato - 2]++;
  }

  console.log("Totale   Frequenza   Percentuale Osservata   Percentuale Attesa");
  console.log("--------------------------------------------------------------");

  for (let totale = 2; totale <= 12; totale++) {
    let percentualeOsservata = (frequenze[totale - 2] / numLanci) * 100;
    let percentualeAttesa = calcolaPercentualeAttesa(totale);

    console.log(`${totale}         ${frequenze[totale - 2]}             ${percentualeOsservata.toFixed(2)}%                   ${percentualeAttesa.toFixed(2)}%`);
  }
}

function calcolaPercentualeAttesa(totale) {
  const frequenzaRelativa = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1];
  const sommaFrequenze = frequenzaRelativa.reduce((acc, val) => acc + val, 0);
  return (frequenzaRelativa[totale - 2] / sommaFrequenze) * 100;
}
  
// Simula 1.000 lanci e visualizza la tabella
simulaLanci(1000);