# A list of players and their scores
players = [("Alice", 50), ("Bob", 90), ("Charlie", 15)]

# Sort by the score (the second item in the pair) in reverse order
top_players = sorted(players, key=lambda x: x[1], reverse=True)

print(top_players)
# Output: [('Bob', 90), ('Alice', 50), ('Charlie', 15)]