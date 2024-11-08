import requests

url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLGamesForWeek"

querystring = {"week":"1","seasonType":"reg","season":"2024"}

headers = {
	"x-rapidapi-key": "2461eb2aafmsh3196f73dc94d982p1b6e48jsnd7c6d23777eb",
	"x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())