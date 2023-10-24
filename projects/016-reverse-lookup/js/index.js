function reverseLookUp(obj, value) {
    const keyCollection = [];

    for (let key in obj) {

        if (obj[key] === value) {
            keyCollection.push(key);
        }
    }

    return keyCollection;
}

const user = {
    name: "Jhon",
    surname: "Red",
    age: 30,
    country: "USA",
    "prefix number": 30,
    best_color: "Red",
}

console.log( reverseLookUp(user, "Red"));