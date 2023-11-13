import React, {useEffect, useState} from 'react';
import classes from "./Container.module.css";
import AnimeAPI from "../../../API/AnimeAPI";
import CharacterItem from "./character_item/CharacterItem";

export function Container() {
  const [data, setData] = useState([])
  const [fetching, setFetching] = useState(true);

  useEffect(() => {
    if (!fetching) {return}

    AnimeAPI.getCharacters().then((response) => {
      console.log(response);
      setData(response);
      setFetching(false);
    });
  }, [fetching]);

  useEffect(() => {

    console.log('[ rfrfz nj');
    document.addEventListener('scroll', scrollHandler)
    return () => {
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
      {
        data.map(item => <CharacterItem key={item.pk} item={item}/>)
      }
    </div>
  );
};
