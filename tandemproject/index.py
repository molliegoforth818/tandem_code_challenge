import os 
from start_quiz import start_quiz
from show_questions import list_of_questions

def build_menu(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print("|  T A N D E M   T R I V I A   Q U I Z |")
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n")
    print("1. Start Quiz")
    print("2. See Questions")
    print("3. Exit ")

def main_menu():
    build_menu()
    while True:
        try:
            print("\nPress number then Enter.")
            choice = int(input("\n>>> "))
            assert 0 < choice <= 3
        except ValueError:
            print("Please enter a number. (1, 2 or 3)")
        except AssertionError:
            print("Please enter either 1, 2 or 3.")
        else:
            break

    if choice == 1:
        start_quiz()
        main_menu()
    if choice == 2:
        list_of_questions()
        main_menu()

    if choice != 3:
        exit()

main_menu()