import random

def main():
    def setup_player():
        name = input("Enter your name: ")
        player = {
            "name": name,
            "health": 10,
            "inventory": []
        }
        return player


    def create_treasures():
        treasures = {
            "gold coin": random.randint(3, 12),
            "ruby": random.randint(3, 12),
            "ancient scroll": random.randint(3, 12),
            "emerald": random.randint(3, 12),
            "silver ring": random.randint(3, 12),
            "diamond": random.randint(3, 12),
            "crown": random.randint(3, 12)
        }
        return treasures


    def display_options(room_number):
        print(f"\nYou are in room {room_number}.")
        print("What would you like to do?")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")


    def search_room(player, treasures):
        outcome = random.choice(["treasure", "trap"])
        if outcome == "treasure":
            found = random.choice(list(treasures.keys()))
            player["inventory"].append(found)
            print(f"You found a {found}! It’s worth {treasures[found]} points.")
        else:
            player["health"] -= 2
            print("A trap! You lose 2 health points!")
        print(f"Current health: {player['health']}")

    def check_status(player):
        print(f"\nHealth: {player['health']}")
        if player["inventory"]:
            print("Inventory:", ", ".join(player["inventory"]))
        else:
            print("Inventory: You have no items yet.")


    def end_game(player, treasures):
        total_value = sum(treasures[item] for item in player["inventory"] if item in treasures)
        print("\n--- Game Summary ---")
        print(f"Final Health: {player['health']}")
        if player["inventory"]:
            print("Collected items:", ", ".join(player["inventory"]))
        else:
            print("No treasures collected.")
        print(f"Total Score (Treasure Value): {total_value}")
        print("\nGame Over! Thanks for playing, adventurer!")


    def run_game_loop(player, treasures):
       for room in range(1, 6):
            if player["health"] < 1:
                print("\nYou’ve lost all your health! 💀")
                break

            while True:
                display_options(room)
                choice = input("Enter your choice (1-4): ")

                if choice == "1":
                    search_room(player, treasures)
                    if player["health"] < 1:
                        print("\nYou have perished in the dungeon!")
                        end_game(player, treasures)
                        return

                elif choice == "2":
                    print("Moving to the next room...")
                    break

                elif choice == "3":
                    check_status(player)

                elif choice == "4":
                    print("\nYou chose to quit early.")
                    end_game(player, treasures)
                    return

                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")

            end_game(player, treasures)


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
