# Sci-Fi Survival Escape on an Alien-Infested Research Station


# Author: Benvindo Kiazayamoko

# Instructions Function

def show_instructions():
    print("---------------------------------------------------")
    print("Sci-Fi Survival Escape on an Alien-Infested Research Station")
    print("----------------------------------------------------")
    print("Collect all 7 components before entering the Escape Shuttle Bay.")
    print("if you enter the villain room too early, the alien will attack.")
    print("\nMove commands: go North, go South, go East, go West")
    print("Add to Inventory: get 'Item Name'")
    print("----------------------------------------------------")

# Status Function

def show_status(current_room, inventory, rooms):
    print("\n.................................")
    print(f"You are in the room {current_room}")
    print(f"Inventory: {inventory}")

    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("-----------------------------------")

# Main game Function

def main():

    # Rooms dictionary (7 items total)

    rooms = {
        "Landing Bay": {
            "North": "Storage Bay",
            "East": "Escape Shuttle Bay"
        },
        "Storage Bay": {
            "North": "Communication Hub",
            "East": "Reaction Room",
            "West": "Engineering Lab",
            "south": "Lading Bay",
            "item": "Fuel Canister"
        },
        "Communication Hub": {
            "East": "Bio Lab",
            "South": "Storage Bay",
            "item": "Navigation Module"
        },
        "Bio Lab": {
            "West": "Communication Hub",
            "item": "Circuit Board"
        },
        "Reaction Room": {
            "North": "Control Room",
            "West": "Storage Bay",
            "item": "Power Cell"
        },
        "Control Room": {
            "South": "Reaction Room",
            "item": "Access Key Card"
        },
        "Engineering Lab": {
            "South": "Cryo Chamber",
            "East": "Storage Bay",
            "item": "Toolkit"
        },
        "Cryo Chamber": {
            "North": "Engineering Lab",
            "item": "Oxygen Regulator"
        },
        "Escape Shuttle Bay": {
            "Villain": "Alien Creature"
        }
    }

    # starting values

    current_room = "Landing Bay"
    inventory = []
    required_items = 7
    game_over = False

    show_instructions()

    # Gameplay loop

    while not game_over:
        show_status(current_room, inventory, rooms)
        command = input("Enter your move: ").strip()

        if len(command) == 0:
            print("Invalid command.")
            continue

        parts = command.split()
        action = parts[0].lower()

        # Movement logic
        if action == "go":
            if len(parts) > 2:
                print("Go where")
                continue


            direction = parts[1].capitalize()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print(f"You move to the {current_room}.")
            else:
                print("You cannot go that way.")

        # Item collection logic

        elif action == "get":
            if len(parts) < 2:
                print("Get what?")
                continue

            item_name = " ".join(parts[1:]).capitalize()

            if "item" in rooms[current_room] and item_name == rooms[current_room]["item"]:
                inventory.append(item_name)
                print(f"{item_name} collection!")
                del rooms[current_room]["item"]
            else:
                print("You cannot get that item.")
        else:
            print("Invalid command.")

        # Win/Lose conditions

        if current_room == "Escape Shuttle Bay":

            if len(inventory) < required_items:
                print("\nThe Alien Creature attacks you!")
                print("Game Over - You failed to escape the station!")
                game_over = True

            else:
                print("\nYou power the shuttle with all collected components!")
                print("You escape the alien-infested research station!")
                print("CONGRATULATIONS! YOU WIN!")
                game_over = True

    print("\nThanks for playing. Hope you enjoyed the adventurer!")

# Run the game

main()










