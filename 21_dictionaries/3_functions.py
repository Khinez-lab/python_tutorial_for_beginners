players = {
    "Messi": { "number": 10, "club": "Barcelona"},
    "Ronaldo": { "number": 7, "club": "Juventus"}
}

# Length
print(len(players))

# Check if item exists
if "Messi" in players:
    print("Messi is in the dict")

# Add item
players["Salah"] = { "number": 11, "club": "Liverpool" }

# Remove
players.pop("Ronaldo")
players.clear()

print(players)