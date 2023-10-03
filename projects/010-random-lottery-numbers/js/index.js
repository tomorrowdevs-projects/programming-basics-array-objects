function getLotteryTicket(quantity = 1) {

    let tickets = "";

    for (let i = 0; i < quantity; i++) {

        const ticket = [];

        while (ticket.length < 6) {

            const ticketNumber = Math.floor( (Math.random() * 49) + 1 );

            if ( !ticket.includes(ticketNumber) ) {
                ticket.push(ticketNumber);
            }

        }

        tickets = ticket + "\n" + tickets;
        
    }

    return tickets;
}

const prompt = require('prompt-sync')({sigint: true});

let wantsTicket;

while (true) {

    wantsTicket = prompt("Desideri paerteciapre alla lotteria? [Si/No] => ");

    wantsTicket = wantsTicket.toLowerCase();

    if (wantsTicket === "si" || wantsTicket === "no") break;

    console.log("Per favore rispondi correttamente.");

}

const response = (wantsTicket === "si") ? prompt("Quanti biglietti vuoi? => ") : "Grazie per la risposta.";

console.log(getLotteryTicket(response) || response);