import os 
import json
import random

def list_of_questions():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("quiz.json") as json_file:
        quiz = json.load(json_file)
        random.shuffle(quiz)
        for d in quiz:
            question = d['question']
            print(f'\n{question}')

    input("\n\nPress Enter to return home.\n\n")