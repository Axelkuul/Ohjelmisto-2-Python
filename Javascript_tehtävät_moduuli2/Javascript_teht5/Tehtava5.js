const lista= []
while (true) {
    const luku = Number(prompt("Anna luku: "))
    if (lista.includes(luku)) {
        alert("Tämä luku on jo listassa! Tulostetaan luvut konsoliin.")
    break
    }
    lista.push(luku)
}
lista.sort()

for (const luku of lista)
console.log(luku)