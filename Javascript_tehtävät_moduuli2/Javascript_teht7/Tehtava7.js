maara = Number(prompt("Mikä on nopan maksimi luku. "));
function heitaNoppaa() {
    return Math.floor(Math.random() * maara) + 1;
}

const lista = document.getElementById("heitot");

while (true) {
    const tulos = heitaNoppaa();
    
    lista.innerHTML += `<li>${tulos}</li>`;
    
    if (tulos === maara) {
        break;
    }
}
