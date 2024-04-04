const readline = require('readline');

const hiddenPassword = (() => {
    const part1 = String.fromCharCode(119, 51, 108, 99, 48, 109, 51);
    const part2 = String.fromCharCode(95, 116, 48);
    const part3 = String.fromCharCode(95, 109, 121);
    const part4 = String.fromCharCode(95, 99, 97, 109, 112);
    return part1 + part2 + part3 + part4;
})();

let revealedCharacters = [];
let totalAttempts = 0;

// Function to check if the password is correct
function checkPassword() {
    totalAttempts++;
    const remainingAttempts = 1000 - (totalAttempts % 1000);
    const readlineInterface = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    readlineInterface.question('Enter the password (You have ' + remainingAttempts + ' attempts left): ', (inputPassword) => {
        if (inputPassword === hiddenPassword) {
            console.log("Congratulations! You have entered the correct password.");
            readlineInterface.close();
        } else {
            console.log("Incorrect password. Try again.");
            readlineInterface.close();
            if (totalAttempts % 1000 === 0 && revealedCharacters.length < 4) {
                const indexToReveal = revealedCharacters.length;
                revealedCharacters.push(hiddenPassword[indexToReveal]);
                console.log("You've revealed a character of the password:", revealedCharacters.join(""));
            }
            if (revealedCharacters.length === 4) {
                console.log("You've revealed all characters of the password. Resetting...");
                revealedCharacters = [];
                totalAttempts = 0;
            }
            checkPassword();
        }
    });
}

// Start the password checking process
checkPassword();


