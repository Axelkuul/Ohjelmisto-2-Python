const nimet = [""];



for(let i = 0; i < 5; i++){
    nimet.push(prompt("Anna nimi: "))
}
document.write(nimet)

document.querySelector("#testi").innerHTML = nimet;
document.querySelector("#vika").innerHTML = taulukko[taulukko.leght-1];
document.querySelector("#sort").innerHTML = taulukko[0];
document.querySelector("#muokattu").innerHTML = taulukko;