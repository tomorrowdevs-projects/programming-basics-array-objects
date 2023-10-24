function calcRollingDice() {
    const dice1Roll = Math.floor( (Math.random() * 6) + 1);
    const dice2Roll = Math.floor( (Math.random() * 6) + 1);

    return dice1Roll + dice2Roll;
}


const tableOfTotal = {
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
    9 : 0,
    10 : 0,
    11 : 0,
    12 : 0,
};

for (let i = 0; i < 1000; i++) {
    const total = calcRollingDice();
    tableOfTotal[total] += 1;
}
console.log(tableOfTotal);
console.log("Frequency for each total on 1000 rolls:");

for (let total in tableOfTotal) {
    const percentage = (tableOfTotal[total] / 10) + " %";
    console.log(total + " : " + percentage);
}