function isRequired() { 
    throw new Error("List must contains at least one item."); 
}

function getFormattedList(array = isRequired()) {

    const itemsNumber = array.length;

    if (itemsNumber === 0) isRequired();

    if (itemsNumber === 1) return array.toString();

    else if (itemsNumber === 2) {

        return array.join(" and ");

    }
    else {
        array.push( getFormattedList( array.splice(-2, 2) ) );

        return array.join(", ");

    }

}


const prompt = require('prompt-sync')({sigint: true});

const list = [];

for (let i = 0; ; i++) {
    const listItem = prompt("Elemento della lista: => ");

    if (listItem === "") break;

    list[i] = listItem;
}

console.log( getFormattedList(list) );