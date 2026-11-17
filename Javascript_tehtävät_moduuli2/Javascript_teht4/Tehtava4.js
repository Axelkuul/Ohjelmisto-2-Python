const lista = []
while (true) {
    const luku = Number(prompt("Anna luku, luku 0 pysäyttää ohjelman ja tulostaa luvut."))
    if (luku == 0) {
        alert("Tulostetaan numerot konsoliin.")
    break
}
lista.push(luku)
}
lista.sort((a, b) => b - a)

console.log(lista)