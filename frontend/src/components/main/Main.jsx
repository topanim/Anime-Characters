import React from 'react';
import {Container} from "./content/Container";
import AnimeAPI from '../../API/AnimeAPI';

export const Main = () => {
	const response = AnimeAPI.getCharacters();
	console.log(response)


  return (
    <main>
      <Container/>
    </main>
  );
};