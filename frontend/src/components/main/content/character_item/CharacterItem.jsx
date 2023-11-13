import React from 'react';
import classes from "./CharacterItem.module.css";
import AnimeAPI from "../../../../API/AnimeAPI";

function CharacterItem({item}){

  const hero = item.fields
  const animeName = AnimeAPI.getAnimeNameById(hero.anime)
  console.log(`zig hail${animeName}`);
  const url = AnimeAPI.getCharacterImageUrl(hero.image)

  return (
    <div className={classes.item} style={{
      background: `linear-gradient(45deg, ${hero.bottom_color} ${hero.bottom}, ${hero.top_color} ${hero.top})`
    }}>
      <div className={classes.hero}>
        <div className={classes.hero_icon_block}>
          <img alt="Hero icon" className={classes.hero_icon} src={url}/>
        </div>
        <div className={classes.about}>
          <p className={classes.hero_name}>{hero.name}</p>
          <p className={classes.hero_about}><strong>Anime: </strong>{animeName}</p>
        </div>
        <p className={classes.read_more}>READ MORE</p>
      </div>
    </div>
  );
};

export default CharacterItem;