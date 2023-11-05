const main = document.querySelector('.content');
console.log(main);
const data_path = "https://api.jsonbin.io/v3/b/65469f0412a5d3765994e4a0"
fetch(data_path)
  .then(file => file.json())
  .then(data => data.record.forEach((hero) => {
	console.log(`background: linear-gradient(45deg, ${hero.bottom_color} ${hero.bottom}, ${hero.top_color} ${hero.top});`);
	let item = `
    <div class="item" style="background: linear-gradient(45deg, ${hero.bottom_color} ${hero.bottom}, ${hero.top_color} ${hero.top});">
      <div class="hero">
        <div class="hero-icon-block">
          <img class="hero-icon" src="${hero.icon}">
        </div>
        <div class="about">
          <p class="hero-name">${hero.name}</p>
          <p class="hero-about"><strong>Anime:</strong> ${hero.anime}</p>
        </div>
        <a class="learn-more" href="${hero.about}" target="_blank">LEARN MORE</a>
      </div>
    </div>`;
  	main.insertAdjacentHTML("beforeEnd", item);
  }));