import os 
# from start_quiz import start_quiz
from show_questions import list_of_questions

def build_menu(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print("|  T A N D E M   T R I V I A  |")
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n")
    print("1. Start Quiz")
    print("2. See Questions")
    print("3. Exit ")

def main_menu():

    build_menu()
    choice = input(">_ ")

    # if choice == "1":
      # start_quiz()

    if choice == "2":
        list_of_questions()
        main_menu()

    if choice != "3":
        exit()

main_menu()