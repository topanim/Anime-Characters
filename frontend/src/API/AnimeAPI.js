// import axios from "axios";

import axios from "axios";

class AnimeAPI {
		static getCharacters(page=1) {
				return axios.get(`${process.env.REACT_APP_BASE_URL}/hero/all?page=${page}`)
					.then(response => response.data)
		}

		static getCharacterImageUrl(image_url) {
			return `${process.env.REACT_APP_BASE_URL}/media/${image_url}`
		}



		static async getAnimeNameById(id) {
			return await axios.get(`${process.env.REACT_APP_BASE_URL}/anime/${id}`)
				.then(response => response.data[0].fields.name)
				.catch(e => console.log(e))
		}
}

export default AnimeAPI;
