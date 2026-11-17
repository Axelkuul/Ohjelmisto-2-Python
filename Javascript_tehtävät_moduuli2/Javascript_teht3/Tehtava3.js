const koirat = []
for (i = 0; i < 6 ; ++ i) {
    const nimet = prompt("Anna koiran nimi");
    koirat.push(nimet)
}
koirat.sort()
koirat.reverse()

html = `<ul><li>${koirat.join("</li><li>")}</li></ul>`;

document.getElementById("vastaus").innerHTML = html;