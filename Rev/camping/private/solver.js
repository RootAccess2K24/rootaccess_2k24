function solveHiddenPassword() {
    const part1 = String.fromCharCode(119, 51, 108, 99, 48, 109, 51);
    const part2 = String.fromCharCode(95, 116, 48);
    const part3 = String.fromCharCode(95, 109, 121);
    const part4 = String.fromCharCode(95, 99, 97, 109, 112);

    return part1 + part2 + part3 + part4;
}

// Call the function to solve the hidden password
const password = solveHiddenPassword();
console.log("Hidden Password:", password);
