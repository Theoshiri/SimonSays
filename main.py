# Import necessary modules
import random   # Used for generating random colors
import time     # Used for adding delays between color displays


colors = ['Red', 'Blue', 'Green', 'Yellow']     # Define a list of colors
score = 0       # Initialize the player score to 0
pattern = []    # Create an empty list to store "color pattern"
stage = 1       # Initialize current stage counter to 1


# Function to randomly select a color from the 'colors' list, then add to the 'pattern' list
def generate_pattern():
    pattern.append(random.choice(colors))


# Function to iterate over each color in the 'pattern' list and print to the console (Use clear_screen function to clear the console after each print)
def display_pattern():
    print("Stage", stage)   # Notify the player what stage they are on
    time.sleep(1)
    clear_screen()

    for color in pattern:
        print(color)
        time.sleep(1)
        clear_screen()


# Function that clears the console screen
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')    # 'cls' for Windows / 'clear' for Unix-based systems


# Function that prompts the player to enter the colors in the 'pattern' list
def get_player_input():
    input_pattern = []

    # Loops through the 'pattern' list, asks the player to input the color which will then be stored in the 'input_pattern' list
    for _ in range(len(pattern)):
        color = input("Enter the color: ")
        input_pattern.append(color)

    return input_pattern


# Function to compare the 'input_pattern' list to the 'pattern' list. If they match, increment a stage and the player score. Else, it's 'Game Over'
def check_pattern(input_pattern):
    global score
    global stage

    if input_pattern == pattern:
        score += 1  # Increment
        stage += 1  # Increment
        print("Correct!")
        time.sleep(1)
        clear_screen()
    else:
        print("Incorrect! Game Over. Your score was:", score)   # Print out player score
        exit()  # Ends the program


# Main Game loop; Displays the welcome message, instructions, and repeatedly generates a new color in the pattern. This is displayed, takes the player input and checks if it matches the pattern. The loop continues until the player makes a mistake
def play_game():
    print("Welcome to Simon Says!")
    time.sleep(1)
    print("Repeat the pattern by entering the colors.")
    time.sleep(1)
    print("Get ready...")
    time.sleep(2)
    clear_screen()

    while True:
        generate_pattern()  # Generate Simon's pattern
        display_pattern()   # Displays the color in succession
        input_pattern = get_player_input()  # Takes player's input and stores it for later comparison
        check_pattern(input_pattern)    # Compares the pattern to the player's pattern and determines a success or fail


# Function called to start the game of 'Simon Says'
play_game()