const nimet = ["John", "Paul", "Jones"];

const targetElement = document.querySelector("#target");

for (let i = 0; i < nimet.length; i++) {
    targetElement.innerHTML += `<li>${nimet[i]}</li>`;
}