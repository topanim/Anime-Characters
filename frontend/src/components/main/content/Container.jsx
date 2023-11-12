import React, {useEffect, useState} from 'react';
import classes from "./Container.module.css";
import {AnimeAPI} from "../../../API/AnimeAPI";
import CharacterItem from "./character_item/CharacterItem";

const Container = () => {
  const [data, setData] = useState([])
  const [fetching, setFetching] = useState(true);

  useEffect((fetching) => {
    console.log(fetching)

    if (!fetching) {return}

    AnimeAPI.testGetCharacters().then((response) => {
      setData(response.data);
      setFetching(false);
    });
  }, [fetching]);

  useEffect(() => {
    document.addEventListener('scroll', scrollHandler)

    return function() {
      document.removeEventListener('scroll', scrollHandler)
    }
  }, []);

  const scrollHandler = (e) => {
    if (e.target.documentElement.scrollHeight - (e.target.documentElement.scrollTop + window.innerHeight) < 200) {
      setFetching(true)
    }
  }

  return (
    <div className={classes.container}>
      <CharacterItem data='' />
    </div>
  );
};

export default Container;