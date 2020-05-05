players = {
    "Messi": { "number": 10, "club": "Barcelona"},
    "Ronaldo": { "number": 7, "club": "Juventus"}
}

print(players["Messi"])
print(players.get("Messi"))

for key in players:
    print(key)

for value in players.values():
    print(value)

for key, value in players.items():
    print(key, value)
