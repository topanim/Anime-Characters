import React from 'react';
import Container from "./content/Container";
import AnimeAPI from '../API/AnimeAPI';

const Main = () => {
	const api = AnimeAPI()
	api.testGetCharacters()
  return (
    <main>
      <Container/>
    </main>
  );
};

export default Main;