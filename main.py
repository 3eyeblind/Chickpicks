# import requests

# # Fetch the NFL team schedule
# schedule_url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeamSchedule"

# schedule_querystring = {"teamAbv":"BUF","season":"2023"}

# headers = {
# 	"x-rapidapi-key": "2461eb2aafmsh3196f73dc94d982p1b6e48jsnd7c6d23777eb",
# 	"x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
# }

# schedule_response = requests.get(schedule_url, headers=headers, params=schedule_querystring)

# # Fetch the NFL betting odds
# odds_url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLBettingOdds"

# odds_querystring = {"gameDate":"20240908","itemFormat":"list","impliedTotals":"true"}

# odds_response = requests.get(odds_url, headers=headers, params=odds_querystring)

# # Print both responses
# print("Team Schedule:")
# print(schedule_response.json())

# print("\nBetting Odds:")
# print(odds_response.json())

import requests

url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeamSchedule"

querystring = {"teamAbv":"PIT","season":"2024"}

headers = {
	"x-rapidapi-key": "2461eb2aafmsh3196f73dc94d982p1b6e48jsnd7c6d23777eb",
	"x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())