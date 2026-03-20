# 🛸 Sci‑Fi Survival Escape — Python Text Adventure Game
**Author:** Benvindo Kiazayamoko  
**Category:** Python Programming • Cybersecurity Learning Project

---

## 🔍 Overview
This project is a Python-based text adventure game set on an alien‑infested research station.  
Your mission: navigate through multiple rooms, collect all 7 survival components, and escape before the alien attacks.

This project demonstrates:
- Python control flow  
- Dictionaries for room mapping  
- Inventory management  
- User input handling  
- Win/Lose logic  
- Modular programming (functions for instructions, status, and main loop)

---

## 🧠 Why This Project Matters for Cybersecurity
Python is one of the most valuable tools in cybersecurity because it teaches:
- **Logical thinking**  
- **Automation skills**  
- **Scripting for security tasks**  
- **Incident simulation and game‑based threat modeling**  

This game is a fun way to practice the same logic used in:
- Network traversal  
- Attack/defense simulations  
- Log analysis  
- Security automation scripts  

---

## 🗺️ Game Features
- 9 interconnected rooms  
- 7 collectible survival items  
- Alien attack fail condition  
- Escape win condition  
- Clear movement and item commands  
- Status updates each turn

---

## 🧩 How to Play
Run the game in any Python environment:

```bash
python game.py

Commands:
Go North, go South, go East, go West
get Item Name
Collect all 7 items before entering the Escape Shuttle Bay.

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


Pseudocode

SET currentRoom = “Landing Bay”
SET inventory = empty list
SET gameOver = False

WHILE gameOver == False:
             DISPLAY “You are in the “ + currentRoom
             DISPLAY “Enter a direction (North, South, East, West):”
             GET direction

             IF currentRoom == “Landing Bay”:
                        IF direction == “North”:
                                 currentRoom = “Storage Bay”
                        ELIF direction == “East”:
                                 currentRoom = “Escape Shuttle Bay”
                        Else:
                                  DISPLAY “You cannot go that way.”
             
            ELIF currentRoom == “Storage Bay”:
                         IF direction == “North”:
                                   currentRoom = “communication Hub”
                         ELIF direction == “East”:
                                   currentRoom == “Reaction Room”
                         ELIF direction == “West”:
                                   currentRoom = “Engineering Lab”
                         ELIF direction == “South”:
                                   currentRoom = “Landing Bay”
                         Else:
                                   DISPLAY “You cannot go that way.”

              ELIF currentRoom == “Communication Hub”:
                          IF direction == “East”:
                                   currentRoom = “Bio Lab”
                          ELIF direction == “South”:
                                   currentRoom = “Storage Bay”
                          ELSE:
                                    DISPLAY “You cannot go that way.”
              
               ELIF currentRoom == “Bio Lab”:
                           IF direction == “West”:
                                    currentRoom = Communication Hub”
                           ELSE:
                                     DISPLAY “You cannot go that way.”
               
               ELIF currentRoom == “Reaction Room”:
                            IF direction == “North”:
                                     currentRoom = “Control Room”
                            ELIF direction == “West”:
                                     currentRoom = “Storage Bay”
                            ELSE:
                                      DISPLAY “You cannot go that way.”
                            
                ELIF currentRoom == “Control Room”:
                              IF direction == “South”:
                                          currentRoom = “Reaction Room”
                              ELSE:
                                          DISPLAY “You cannot go that way.”

                ELIF currentRoom == “Engineering Lab”:
                              IF direction == “South”:
                                            currentRoom = “Cryo Chamber”
                              ELIF direction == “East”:
                                            currentRoom = “Storage Bay”
                             ELSE:
                                            DISPLAY “You cannot go that way.”

                ELIF currentRoom == “Cryo Chamber”:
                              IF direction == “North”:
                                              currentRoom = “Engineering Lab”
                              ELSE:
                                           DISPLAY “You cannot go that way.”
                             
                             DISPLAY “You moved to the” + currentRoom

                IF currentRoom == “Escape Shuttle Bay” AND inventory does not contain all 6 items: 
                            DISPLAY “The alien attacks you! Game Over.”
                            SET gameOver = True
                IF currrentRoom == “Escape Shuttle Bay” AND inventory contains all 6 items:
                            DISPLAY “You power the shuttle and escape! You win
                            SET gameOver = True
END WHILE

Flowchard

<img width="1019" height="915" alt="image" src="https://github.com/user-attachments/assets/d56ae22f-5ef6-4b3b-96ec-fec3cb7e7487" />

This project combines creativity, programming logic, and cybersecurity thinking.
It demonstrates how Python can be used to build simulations, automate tasks, and strengthen problem‑solving skills essential for the cybersecurity field.




