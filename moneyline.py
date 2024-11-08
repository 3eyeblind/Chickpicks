# import requests

# url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeamSchedule"
# querystring = {"teamAbv": "PIT", "season": "2024"}
# headers = {
#     "x-rapidapi-key": "2461eb2aafmsh3196f73dc94d982p1b6e48jsnd7c6d23777eb",
#     "x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# # Extract schedule data from the response
# schedule_data = response.json().get('body', {}).get('schedule', [])

# # Initialize win and loss counters
# wins = 0
# losses = 0

# # Loop through each game in the schedule, counting only "Completed" games
# for game in schedule_data:
#     if game.get('gameStatus') == 'Completed':  # Updated to match "gameStatus": "Completed"
#         if game.get('home') == 'PIT':
#             if game.get('homeResult') == 'W':
#                 wins += 1
#             elif game.get('homeResult') == 'L':
#                 losses += 1
#         elif game.get('away') == 'PIT':
#             if game.get('awayResult') == 'W':
#                 wins += 1
#             elif game.get('awayResult') == 'L':
#                 losses += 1

# # Calculate the win-loss ratio
# if losses > 0:
#     ratio = wins / losses
# else:
#     ratio = wins  # if there are no losses, the ratio is simply the number of wins

# print(f"Wins: {wins}, Losses: {losses}, Win-Loss Ratio: {ratio:.2f}")


import requests

url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeamSchedule"
querystring = {"teamAbv": "PIT", "season": "2024"}
headers = {
    "x-rapidapi-key": "2461eb2aafmsh3196f73dc94d982p1b6e48jsnd7c6d23777eb",
    "x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Extract schedule data from the response
schedule_data = response.json().get('body', {}).get('schedule', [])

# Initialize win and loss counters
wins = 0
losses = 0

# Loop through each game in the schedule, counting only "Completed" regular season games
for game in schedule_data:
    if game.get('gameStatus') == 'Completed' and game.get('seasonType') == 'Regular Season':
        if game.get('home') == 'PIT':
            if game.get('homeResult') == 'W':
                wins += 1
            elif game.get('homeResult') == 'L':
                losses += 1
        elif game.get('away') == 'PIT':
            if game.get('awayResult') == 'W':
                wins += 1
            elif game.get('awayResult') == 'L':
                losses += 1

# Calculate the win-loss ratio
if losses > 0:
    ratio = wins / losses
else:
    ratio = wins  # if there are no losses, the ratio is simply the number of wins

print(f"Wins: {wins}, Losses: {losses}, Win-Loss Ratio: {ratio:.2f}")
