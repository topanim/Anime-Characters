// import axios from "axios";

import axios from "axios";

class AnimeAPI {
		static getCharacters() {
				return axios.get(`${process.env.REACT_APP_BASE_URL}/hero/all`)
					.then(response => response.data)
		}

		static getCharacterImageUrl(image_url) {
			const url = `${process.env.REACT_APP_BASE_URL}/media/${image_url}`
			console.log(url)
			return url
		}



		static getAnimeNameById(id) {
			return axios.get(`${process.env.REACT_APP_BASE_URL}/anime/${id}`)
				.then(response => {
					console.log(`${process.env.REACT_APP_BASE_URL}/anime/${id}`);
					console.log(response.data);
					console.log(response.data[0].fields.name);
					console.log(response.data[0].fields.name.type);
					return response.data
				})
		}
}

export default AnimeAPI;
