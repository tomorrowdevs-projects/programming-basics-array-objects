function checkSublist(list1, list2) {
    if (list2 == "") return true;

    // Check if the second list items are included or not in the first list and also automatically exclude all the lists longer than the first
    if ( list2.every(isIncluded) ) { 
        
        if (list1.length === list2.length) return true; // This case validate identical list
        
        // To easy compair a sublist of an array with onother array, I transform they to a string type
        const stringfyList1 = list1.toString();
        const stringfyList2 = list2.toString();

        const sublist = stringfyList1.match(stringfyList2);

        if (sublist !== null) return true; // To validate adjacent items
    }
    
    return false;

    function isIncluded(item) {
       return list1.includes(item);
    }
}

const list1 = [1, 2, 3, 4];
const list2 = [2, 1];

const result = ( checkSublist(list1, list2) ) ? "è" : "non è";

console.log("Lista 1: => " + list1);
console.log("Lista 2: => " + list2);
console.log("La lista 2 " + result + " una sottolista della prima lista.");

// Solution2

// function checkSublist(list1, list2) {
//     if (list2 == "") return true;

//     // Check if the second list items are included or not in the first list and also automatically exclude all the lists longer than the first
//     if ( list2.every(isIncluded) ) { 
        
//         if (list1.length === list2.length) return true; // This case validate identical list
        
//         const sublistStart = list1.indexOf(list2[0]);
//         const sublistEnd = list1.indexOf(list2.at(-1));
        
//         const sublist = list1.slice(sublistStart, sublistEnd + 1);

//         if (sublist.length === list2.length) return true;

//     }
    
//     return false;

//     function isIncluded(item) {
//        return list1.includes(item);
//     }
// }

// const list1 = [1, 2, 3, 4];
// const list2 = [2, 1];

// const result = ( checkSublist(list1, list2) ) ? "è" : "non è";

// console.log("Lista 1: => " + list1);
// console.log("Lista 2: => " + list2);
// console.log("La lista 2 " + result + " una sottolista della prima lista.");