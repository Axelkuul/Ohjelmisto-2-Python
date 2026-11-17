const lista = []
maara = Number(prompt("Kuinka monta osallistujaa"));
for (let i = 0; i < maara ; i++) {
    let nimi = prompt("Anna osallistujan nimi: ")
    lista.push(nimi)
}
lista.sort()
const html = `<ol><li>${lista.join("</li><li>")}</li></ol>`;

document.getElementById("vastaus").innerHTML = html;