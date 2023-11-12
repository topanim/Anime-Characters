// import axios from "axios";

import axios from "axios";

export class AnimeAPI {
		static testGetCharacters() {
				return axios.get(`${process.env.REACT_APP_BASE_URL}/hero/all`)
					.then(response => response.data.record)
		}

		static testGetAnimeAll() {
			
		}
}
