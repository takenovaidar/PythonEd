import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_field():
    return [[" " for _ in range(7)] for _ in range(7)]

def display_field(field, hide_ships=False):
    print("  1 2 3 4 5 6 7")
    for i, row in enumerate(field):
        row_to_display = [
            cell if not hide_ships or cell not in {"S"} else "~"
            for cell in row
        ]
        print(chr(65 + i), " ".join(row_to_display))

def is_valid_placement(field, ship, row, col, direction):
    for i in range(len(ship)):
        r = row + (i if direction == "V" else 0)
        c = col + (i if direction == "H" else 0)

        if not (0 <= r < 7 and 0 <= c < 7): 
            return False
        if field[r][c] != " ":  
            return False
        
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                nr, nc = r + dr, c + dc
                if 0 <= nr < 7 and 0 <= nc < 7 and field[nr][nc] == "S":
                    return False
    return True

def place_ship(field, ship):
    while True:
        row, col = random.randint(0, 6), random.randint(0, 6)
        direction = random.choice(["H", "V"])  
        if is_valid_placement(field, ship, row, col, direction):
            for i in range(len(ship)):
                r = row + (i if direction == "V" else 0)
                c = col + (i if direction == "H" else 0)
                field[r][c] = ship[i]
            return

def place_all_ships(field):
    ships = [3, 2, 2, 1, 1, 1, 1]  
    for ship_size in ships:
        place_ship(field, ["S"] * ship_size)

def all_ships_sunk(field):
    for row in field:
        if "S" in row:
            return False
    return True

def get_player_input():
    while True:
        shot = input("Enter your shot (e.g., B5): ").upper()
        if len(shot) == 2 and shot[0].isalpha() and shot[1].isdigit():
            row = ord(shot[0]) - ord("A")
            col = int(shot[1]) - 1
            if 0 <= row < 7 and 0 <= col < 7:
                return row, col
        print("Invalid input. Try again.")

def handle_shot(field, row, col, visible_field):
    if visible_field[row][col] != "~":
        return "already"  
    if field[row][col] == "S":
        visible_field[row][col] = "⊡" 
        field[row][col] = "⊡"
        if is_ship_sunk(field, row, col): 
            mark_sunk_ship(visible_field, field)
        return "hit"
    else:
        visible_field[row][col] = "⊙"  
        return "miss"

def is_ship_sunk(field, row, col):
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            nr, nc = row + dr, col + dc
            if 0 <= nr < 7 and 0 <= nc < 7 and field[nr][nc] == "S":
                return False
    return True

def mark_sunk_ship(visible_field, field):
    for r in range(7):
        for c in range(7):
            if field[r][c] == "⊡": 
                if is_ship_sunk(field, r, c):
                    for dr in range(-6, 7):  
                        for dc in range(-6, 7):
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < 7 and 0 <= nc < 7 and field[nr][nc] == "⊡":
                                visible_field[nr][nc] = "⊠"

leaderboard = {}

def update_leaderboard(name, shots):
    """Update the leaderboard with the player's name and score."""
    if name in leaderboard:
        leaderboard[name] = min(leaderboard[name], shots)  
    else:
        leaderboard[name] = shots

def display_leaderboard():
    """Display the sorted leaderboard."""
    if not leaderboard:
        print("No players on the leaderboard yet!")
        return
    print("\nLeaderboard:")
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1])
    for rank, (name, score) in enumerate(sorted_leaderboard, start=1):
        print(f"{rank}. {name}: {score} shots")

def main():
    while True:
        clear_screen()
        print("Welcome to Battleship!")
        player_name = input("Enter your name: ")
        field = create_field()
        visible_field = [["~" for _ in range(7)] for _ in range(7)]  
        place_all_ships(field)

        shots = 0
        while True:
            clear_screen()
            print(f"Player: {player_name}")
            display_field(visible_field)
            row, col = get_player_input()
            result = handle_shot(field, row, col, visible_field)
            if result == "hit":
                print("It's a hit!")
            elif result == "miss":
                print("You missed!")
            elif result == "already":
                print("You already shot here.")
            shots += 1

            if all_ships_sunk(field):
                clear_screen()
                print(f"Congratulations, {player_name}! You sank all the ships in {shots} shots!")
                update_leaderboard(player_name, shots) 
                break

        if input("Play again? (YES/NO): ").upper() != "YES":
            clear_screen()
            display_leaderboard() 
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()