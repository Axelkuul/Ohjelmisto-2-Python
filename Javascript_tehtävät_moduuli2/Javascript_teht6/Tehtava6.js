function heitaNoppaa() {
    return Math.floor(Math.random() * 6) + 1;
}

const lista = document.getElementById("heitot");

while (true) {
    const tulos = heitaNoppaa();
    
    lista.innerHTML += `<li>${tulos}</li>`;
    
    if (tulos === 6) {
        break;
    }
}
