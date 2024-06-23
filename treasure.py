import random 

 

# Constants 

MAX_DIMENSION = 4 

MIN_DIMENSION = 4 

MISS_SYMBOL = 8 

HIT_SYMBOL = 1 

MAX_STRIKES = 3 

ADMIN_PASSWORD = "password" 

 

# Function to get user's name 

def get_user_name(): 

    return input("Enter your name: ") 

 

# Function to print highscores 

def print_highscores(highscores): 

    if not highscores: 

        print("No highscores yet.") 

    else: 

        print("\nHighscores:") 

        for score in highscores: 

            print(f"{score['name']}: {score['score']} attempts: {score['dimension']}") 

 

# Function to initialize the game board with zeros 

def initialize_board(board_dimension): 

    return [[0] * board_dimension for _ in range(board_dimension)] 

 

# Function to display the game board 

def display_board(board): 

    print("   ", end="") 

    for i in range(1, len(board) + 1): 

        print(f"{i:3}", end="") 

    print("\n  " + " ".join(["-" * 3] * len(board))) 

    for i, row in enumerate(board): 

        print(chr(65 + i), end=" ") 

        for val in row: 

            print(f"{val:3}", end="") 

        print() 

 

def play_game(board_dimension, admin_mode): 

    game_board = initialize_board(board_dimension) 

    treasure_row = random.randint(0, board_dimension - 1) 

    treasure_col = random.randint(0, board_dimension - 1) 

    if admin_mode: 

        print(f"\nAdmin mode enabled. The treasure is at: {chr(65 + treasure_row)}{treasure_col + 1}") 

    print(f"\nWelcome to the treasure hunt ({board_dimension}x{board_dimension})\n") 

    display_board(game_board) 

    attempts = 0 

    strikes = 0  # Counter for strikes 

    while True: 

        user_input = input("\nEnter position (A1-D4): ").strip().upper() 

        # Check if user input is empty 

        if not user_input: 

            print("You didn't enter a guess. Please enter a valid position.") 

            continue  # Continue to next iteration of the game loop 

        # Check if user input is in valid format 

        if user_input[0] not in ['A', 'B', 'C', 'D'] or not user_input[1].isdigit() or len(user_input) != 2: 

            print("Invalid guess format. Please enter a valid position (A1-D4).") 

            strikes += 1  # Increment strikes counter 

            if strikes >= MAX_STRIKES:  # Check if maximum strikes reached 

                print("You've exceeded the maximum number of strikes. Game over.") 

                break  # Break out of the game loop 

            continue  # Continue to next iteration of the game loop 

        row = ord(user_input[0]) - 65 

        col = int(user_input[1]) - 1 

        # Check if user input is within board bounds 

        if not (0 <= row < board_dimension and 0 <= col < board_dimension): 

            print("Position is out of bounds. Please enter a valid position (A1-D4).") 

            strikes += 1  # Increment strikes counter 

            if strikes >= MAX_STRIKES:  # Check if maximum strikes reached 

                print("You've exceeded the maximum number of strikes. Game over.") 

                break  # Break out of the game loop 

            continue  # Continue to next iteration of the game loop 

        attempts += 1 

        if (row, col) == (treasure_row, treasure_col): 

            print("\nCongratulations! You found the treasure!") 

            print(f"Number of attempts: {attempts}") 

            game_board[row][col] = HIT_SYMBOL 

            display_board(game_board) 

            return attempts 

        else: 

            print("\nOops! That's a miss.") 

            game_board[row][col] = MISS_SYMBOL 

            display_board(game_board) 

 

# Function to display game instructions 

def instructions(): 

    print("\nInstructions:") 

    print("Welcome to the Treasure Hunt Game!") 

    print("In this game, you'll be searching for a hidden treasure on a game board.") 

    print("The game board is represented as a grid, with rows labeled A, B, C, D, and columns numbered 1, 2, 3, 4.") 

    print("Your task is to guess the position of the treasure by entering coordinates in the format A1, B2, etc.") 

    print("Each time you enter a position, the game will tell you if you've found the treasure or not.") 

    print("You win the game when you find the treasure.") 

    print("You can also view highscores, enter admin mode and exit the game from the main menu.") 

    print("Have fun and happy hunting!") 

 

# Main function 

def main(): 

    print("Welcome to the Treasure Hunt Game!\n") 

    name = get_user_name() 

    highscores = [] 

    admin_mode = False 

    # Main menu loop 

    while True: 

        print("\nDashboard:") 

        print("1. Start Game") 

        print("2. Highscores") 

        print("3. Instructions") 

        print("4. Admin Mode") 

        print("5. Exit") 

        choice = input("\nEnter your choice: ") 

        # Start Game 

        if choice == '1': 

            dimension = 4 

            score = play_game(dimension, admin_mode) 

            if score: 

                highscores.append({'name': name, 'score': score, 'dimension': f"{dimension}x{dimension}"}) 

        # Highscores 

        elif choice == '2': 

            print_highscores(highscores) 

        # Instructions 

        elif choice == '3': 

            instructions() 

        # Admin Mode 

        elif choice == '4': 

            admin_choice = input("Do you want to enable admin mode? (yes/no): ").lower() 

            if admin_choice == "yes": 

                admin_mode = True 

                print("Admin mode enabled.") 

            elif admin_choice == "no": 

                admin_mode = False 

                print("Admin mode disabled.") 

            else: 

                print("Invalid choice!") 

        # Exit 

        elif choice == '5': 

            print("Thanks for playing!") 

            break 

        else: 

            print("Invalid choice! Please enter a valid option.") 

 

# Check if this script is the main one being run 

if __name__ == "__main__": 

    # If it is, execute the main() function 

    main() 