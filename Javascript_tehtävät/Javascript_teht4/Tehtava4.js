const nimi = prompt("Mikä sun nimi on: ");
const tuvat = ["Rohkelikko", "Luihuinen", "Puuskupuh", "Korpinkynsi"];
const arvottu = tuvat[Math.floor(Math.random() * 4)];

document.getElementById("tulos").innerHTML = nimi + ", sinä olet " + arvottu + ".";