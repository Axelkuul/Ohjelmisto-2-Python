'use strict';

const searchForm = document.querySelector('#search-form');

searchForm.addEventListener('submit', async function(event) {
    event.preventDefault();

    const queryValue = document.querySelector('#query').value;

    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${queryValue}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const jsonData = await response.json();
        console.log(jsonData);

    } catch (error) {
        console.error('Error fetching data:', error);
    }
});
