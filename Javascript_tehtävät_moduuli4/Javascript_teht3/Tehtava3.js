'use strict';

const searchForm = document.querySelector('#search-form');
const resultsContainer = document.querySelector('#results');

searchForm.addEventListener('submit', async function(event) {
    event.preventDefault();

    const queryValue = document.querySelector('#query').value;
    resultsContainer.innerHTML = '';

    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${queryValue}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const jsonData = await response.json();

        for (const tvShow of jsonData) {
            const article = document.createElement('article');

            const h2 = document.createElement('h2');
            h2.textContent = tvShow.show.name;

            const link = document.createElement('a');
            link.href = tvShow.show.url;
            link.target = '_blank';
            link.textContent = 'Show details';

            const img = document.createElement('img');
            img.src = tvShow.show.image?.medium || '';
            img.alt = tvShow.show.name;

            const summary = document.createElement('div');
            summary.innerHTML = tvShow.show.summary || '';

            article.append(h2, link, img, summary);
            resultsContainer.append(article);
        }

    } catch (error) {
        console.error('Error fetching data:', error);
    }
});
