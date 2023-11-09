const dotenv = require("dotenv");

class AnimeAPI {
		constructor() {
				this.env = require('dotenv').config().parsed;
		}

		testGetCharacters() {
				fetch(this.env.TEST_URL)
						.then(response => response.json())
						.then(data => {
								console.log(data)
						})
		}
}