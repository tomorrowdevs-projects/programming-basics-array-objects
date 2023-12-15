export function removeExtremities(list, n) {
    let sortedList = [];
    // verify if list contains at least 6 element
    if (list.length < 6) {
        throw new Error("List should contain at least 4 numbers");
    } else {
        // sort list
        sortedList = list.sort((a, b) => a - b);
    
        // Remove the n values, bigger and smaller
        let listWithoutExtr = sortedList.slice(n, -n);
    
        return listWithoutExtr;

    }
}
