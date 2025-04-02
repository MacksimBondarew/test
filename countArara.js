function countArara(n) {
    let arrayArara = [];
    let countRemaining = n;
    while (countRemaining > 0) {
        if (countRemaining - 2 >= 1 || countRemaining - 2 === 0) {
            arrayArara.push("adak");
            countRemaining -= 2;
            console.log(countRemaining);
        } else {
            arrayArara.push("anane");
            break;
        }
    }
    return arrayArara.join(" ");
}