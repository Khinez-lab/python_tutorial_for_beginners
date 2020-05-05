names = { "Mike", "Kate", "Dave" }

# Length
print(len(names))

# Check if item exists
if "Kate" in names:
    print("Kate is in the set")

# Add
names.add("Bob")
names.update(["Ben", "Tod"])

# Remove
names.remove("Kate")
names.discard("Ben")
names.clear()

print(names)