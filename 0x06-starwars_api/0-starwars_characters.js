#!/usr/bin/node

const axios = require('axios');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

const fetchCharacterName = async (characterUrl) => {
  try {
    const response = await axios.get(characterUrl);
    console.log(response.data.name);
  } catch (error) {
    console.error(`Error fetching character data: ${error.message}`);
  }
};

const fetchFilmCharacters = async () => {
  try {
    const response = await axios.get(url);
    const characterUrls = response.data.characters;

    for (const characterUrl of characterUrls) {
      await fetchCharacterName(characterUrl);
    }
  } catch (error) {
    console.error(`Error fetching film data: ${error.message}`);
  }
};

fetchFilmCharacters();
