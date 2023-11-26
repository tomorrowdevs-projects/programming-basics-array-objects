const randomSort = require("./index");

describe('Testing the randomSort function', () => {
    
    test('to return an Array', () => {
        const array = [1,2,3,4];
        expect(Array.isArray(randomSort(array))).toBeTruthy();
    });

    test('to random sort the array in place', () => {
        const array = [1,2,3,4];
        const sortedArray = randomSort(array);
        expect(Object.is(array, sortedArray)).toBe(true);
    });

    test('to work properly with both negative and positive integers', () => {
        const array = [1, 2, 3, 4, 0, -2, -10];
        const sortedArray = randomSort(array);
        expect(sortedArray).toContain(-10);
        expect(sortedArray).not.toBe([1, 2, 3, 4, 0, -2, -10]);
        // console.log(sortedArray);
    });

    test('to work with floats and strings', () => {
        const array = [1.2, 3, -2, 0, -0, -9.7, "Hello", "Alessandro"];
        const sortedArray = randomSort(array);
        expect(sortedArray).toContain(1.2);
        expect(sortedArray).not.toBe([1.2, 3, -2, 0, -0, -9.7, "Hello", "Alessandro"]);
    });

    test('to work with empty, sparse array and nested array', () => {
        const array = [] // void, 0 item
        const emptyArray = [,]; // 1 empty item
        const sparseArray = [,,,2]; // 3 empty items and 1 item
        const nestedArray = [ 1, "hello", [ -2, [0, "dev"], 9.9], "end"];

        expect(randomSort(array)).toHaveLength(0); // 0 item
        expect(randomSort(array)).not.toContain(undefined); // must contain 0 item
        expect(randomSort(array)).toBe(array); // [] remain []
        expect(Object.is(randomSort(array), array)).toBe(true); // sorted in place, same reference
 
        expect(randomSort(emptyArray)).toHaveLength(1); //
        expect(randomSort(emptyArray)).toBe(emptyArray);

        expect(randomSort(sparseArray)).toHaveLength(4);
        expect(randomSort(sparseArray)).toContain(undefined); // when sorted, the empty item become typeof undefined

        expect(randomSort(nestedArray)).not.toBe([ 1, "hello", [ -2, [0, "dev"], 9.9], "end"]);
    });
})