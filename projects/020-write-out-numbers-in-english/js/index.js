function numeroInParole(numero) {
    const numeri = {
      0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
      6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
      11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
      16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    };
  
    const decine = {
      20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
      60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
    };
  
    function convertiDecineUnita(n) {
        if (n < 20) {
            return numeri[n];
        } else {
            const decina = Math.floor(n / 10) * 10;
            const unita = n % 10;
            return (unita !== 0 ? decine[decina] + ' ' + numeri[unita] : decine[decina]);
        }
    }
  
    function convertiInParolePrincipale(numero) {
      if (numero === 0) {
        return 'zero';
      }
  
      let result = '';
  
      if (numero >= 100) {
        const centinaia = Math.floor(numero / 100);
        result += numeri[centinaia] + ' hundred';
        numero %= 100;
  
        if (numero > 0) {
          result += ' ';
        }
      }
  
      if (numero > 0 && numero < 19) {
        result += numeri[numero];
      } else if (numero >= 20) {
        result += convertiDecineUnita(numero);
      }
  
      return result;
    }
  
    return convertiInParolePrincipale(numero);
  }
  
  const numeroInput = parseInt(prompt("Inserisci un numero tra 0 e 999:"));
  
  if (isNaN(numeroInput) || numeroInput < 0 || numeroInput > 999) {
    console.log("Inserisci un numero valido.");
  } else {
    const numeroInParoleOutput = numeroInParole(numeroInput);
    console.log(`Il numero ${numeroInput} in parole è: ${numeroInParoleOutput}`);
  }
  