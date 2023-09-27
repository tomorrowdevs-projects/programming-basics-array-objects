function removeOutliers(dataCollection, number) {

    if (number < 0) {
        throw new Error("Parametro non valido");
    }

    dataCollection.sort(function (p1, p2) {return p1 -p2})

    const cleanDataCollection = dataCollection.slice(number, -number);

    return cleanDataCollection;
}


const prompt = require('prompt-sync')({sigint: true});

const numberCollection = [];
const numbersMinQuantity = 4;
const minmaxValuestoRemove = 2;

while (true) {

    for (let i = 0; true; i++) {
        const number = Number( prompt("Numero: => ") );

        if (number === 0) {
            break;
        }
        
        numberCollection[i] = number;
    }

    const valuesInCollection = numberCollection.length;

    if (valuesInCollection < numbersMinQuantity){
        console.log("Errore! Inserisci almeno 4 numeri.");
    }
    else {
        break;
    }
} 

console.log( removeOutliers(numberCollection, minmaxValuestoRemove) );
console.log(numberCollection);