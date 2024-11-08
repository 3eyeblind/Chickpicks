# import requests

# url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLBettingOdds"

# querystring = {"gameDate":"20240908","itemFormat":"list","impliedTotals":"true"}

# headers = {
# 	"x-rapidapi-key": "2461eb2aafmsh3196f73dc94d982p1b6e48jsnd7c6d23777eb",
# 	"x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

# game_dates = ["20240908", "20240915", "20240922", "20240929", "20241006", "20241013"]

import requests

# List of game dates you want to check (in the format YYYYMMDD)
game_dates = ["20240908", "20240915", "20240922"]

url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLBettingOdds"

headers = {
    "x-rapidapi-key": "2461eb2aafmsh3196f73dc94d982p1b6e48jsnd7c6d23777eb",
    "x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
}

# Loop through the game dates
for game_date in game_dates:
    querystring = {"gameDate": game_date, "itemFormat": "list", "impliedTotals": "true"}
    
    response = requests.get(url, headers=headers, params=querystring)
    games = response.json().get('body', [])
    
    # Filter for PIT games
    pit_games = [game for game in games if game['homeTeam'] == 'PIT' or game['awayTeam'] == 'PIT']
    
    # Print out the PIT games for this game date
    print(f"Games on {game_date}:")
    for game in pit_games:
        # Filter for FanDuel odds only
        fanduel_odds = next((book for book in game['sportsBooks'] if book['sportsBook'].lower() == 'fanduel'), None)
        
        if fanduel_odds:
            print(f"Game: {game['homeTeam']} vs {game['awayTeam']}")
            print(f"FanDuel Odds: {fanduel_odds['odds']}")
        else:
            print(f"No FanDuel odds available for {game['homeTeam']} vs {game['awayTeam']}")
            
    print("\n" + "-"*30 + "\n")
