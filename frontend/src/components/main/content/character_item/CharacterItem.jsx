import React from 'react';
import classes from "./CharacterItem.module.css";

const CharacterItem = ({hero}) => {
  return (
    <div className={classes.item}>
      <div className={classes.hero}>
        <div className={classes.hero_icon_block}>
          <img alt="Hero icon" className={classes.hero_icon} src={hero.src}/>
        </div>
        <div className="about">
          <p className={classes.hero_name}>{hero.name}</p>
          <p className="hero-about"><strong>Anime:</strong>{hero.anime}</p>
        </div>
        <a className={classes.learn_more} href={hero.about} target="_blank">READ MORE</a>
      </div>
    </div>
  );
};

export default CharacterItem;