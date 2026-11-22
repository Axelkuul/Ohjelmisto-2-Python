const opiskelijat = [
  {
    nimi: 'John',
    id: '2345768',
  },
  {
    nimi: 'Paul',
    id: '2134657',
  },
  {
    nimi: 'Jones',
    id: '5423679',
  },
];

const targetElement = document.querySelector('#target');

for (let i = 0; i < opiskelijat.length; i++) {
  const vaihtoehto = document.createElement('option');

  vaihtoehto.value = opiskelijat[i].id;
  vaihtoehto.textContent = opiskelijat[i].nimi;
  
  targetElement.appendChild(vaihtoehto);
}