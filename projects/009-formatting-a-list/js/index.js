function prepareString(items) {
    const listLength = items.length;
    if (listLength === 0) {
        return "The list is empty.";
    } else if(listLength === 1) {
        return items[0];
    } else {
        const joinedList = items.slice(0, listLength - 1).join(', ');
        const result = `${joinedList} and ${items[listLength - 1]}`;

        return result;
    }
}

const userInput = prompt('Enter a list of items separated with a comma:');
const items = userInput.split(',').map(item => item.trim());

const formattedList = prepareString(items);
console.log(`Formatted List: ${formattedList}`);