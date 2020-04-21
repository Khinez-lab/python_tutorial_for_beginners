# ✊🏻 ✋🏻 ✌🏻 🧔 💻 🎉 💀 🏆 ⛔ 🗑

import random

player_thropies = 0
computer_thropies = 0

while player_thropies < 3 and computer_thropies < 3:
    player_hand = input("🧔: ")
    computer_hand = random.randrange(3) # 0, 1, 2

    if (
        player_hand != "✊🏻"
        and player_hand != "✋🏻"
        and player_hand != "✌🏻"
    ):
        print("⛔")
        print("")
        continue

    if computer_hand == 0:
        computer_hand = "✊🏻"
    elif computer_hand == 1:
        computer_hand = "✋🏻"
    else:
        computer_hand = "✌🏻"

    print("💻: " + computer_hand)

    # 0. Draw - Skip round
    # 1. ✊🏻 beats ✌🏻
    # 2. ✋🏻 beats ✊🏻
    # 3. ✌🏻 beats ✋🏻

    if player_hand == computer_hand:
        print("🗑")
        print("")
    elif player_hand == "✊🏻":
        if computer_hand == "✋🏻":
            computer_thropies += 1
            print("You lost! 💀")
        else:
            player_thropies += 1
            print("You won! 🎉")
    elif player_hand == "✋🏻":
        if computer_hand == "✌🏻":
            computer_thropies += 1
            print("You lost! 💀")
        else:
            player_thropies += 1
            print("You won! 🎉")
    elif player_hand == "✌🏻":
        if computer_hand == "✊🏻":
            computer_thropies += 1
            print("You lost! 💀")
        else:
            player_thropies += 1
            print("You won! 🎉")
        pass

    print(player_thropies * "🏆" + " vs. " + computer_thropies * "🏆")
    print("")
