# A list of players and their scores
players = [("abdu", 50), ("Baca", 90), ("chale", 15)]

# Sort by the score (the second item in the pair) in reverse order
top_players = sorted(players, key=lambda x: x[1], reverse=True)

print(top_players)
Output: [('Baca', 90), ('abdu', 50), ('Chale', 15)]