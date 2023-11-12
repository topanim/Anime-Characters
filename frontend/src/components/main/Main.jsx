import React from 'react';
import Container from "./content/Container";
import {AnimeAPI} from '../../API/AnimeAPI';

const Main = () => {
	const response = AnimeAPI.testGetCharacters();
	console.log(response)


  return (
    <main>
      <Container/>
    </main>
  );
};

export default Main;