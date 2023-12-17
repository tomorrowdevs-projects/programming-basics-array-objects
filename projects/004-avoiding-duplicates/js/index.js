let userInput;
const userList = [];

const wordStore = () =>{
    do {
        userInput = prompt('insert a word: ');
        userInput = userInput.trim().toLowerCase();
        if (userInput !== " ") {
            userList.push(userInput);
            
        }

    } while (userInput !== "" && userInput !== " ");

    const uniqueUserList = userList.filter((value, index, self) => {
        return self.indexOf(value) === index;
    });
    console.log('your word list:');
    uniqueUserList.forEach(el => console.log(el));
}

wordStore();