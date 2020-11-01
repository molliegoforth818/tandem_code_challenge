import json
import os 
import random
from answer_list import show_answers
from answer_list import get_answer_list
from scores import correct
from scores import incorrect



def start_quiz():
    score = 0
    with open("quiz.json") as json_file:
        quiz = json.load(json_file)
        random.shuffle(quiz)

        for d in quiz[:10]:
            os.system('cls' if os.name == 'nt' else 'clear')
            question = d['question']
            print(f'[?] {question}')

            answers = get_answer_list(d)

            show_answers(answers)

            # if you check the index of the given answer from answer list against the correct answer which is a prop of 'd'

            while True:
                try:
                    choice = int(input("\n>> "))
                    assert 0 < choice <= len(answers)
                except ValueError:
                    print("Please enter a number.")
                except AssertionError:
                    print(
                        f'Please enter an number between 1 and {len(answers)}')
                else:
                    break

            if choice == 1:
                if answers[0] == d['correct']:
                    correct()
                    score += 1
                else:
                    incorrect(d)

            if choice == 2:
                if answers[1] == d['correct']:
                    correct()
                    score += 1
                else:
                    incorrect(d)

            if choice == 3:
                if answers[2] == d['correct']:
                    correct()
                    score += 1
                else:
                    incorrect(d)

            if choice == 4:
                if answers[3] == d['correct']:
                    correct()
                    score += 1
                else:
                    incorrect(d)

    if score == 10:
        print(
            f'Wow {score}/10\nPerfect Score!\n')
        input("Press Enter to return to home menu.")
    if score == 9:
        print(
            f'Almost a perfect score! {score}/10\nThere is always next time!.\n')
        input("Press Enter to return to home menu.")
    if 6 < score < 9:
        print(
            f'Great effort!\nYou need higher than {score}/10\n')
        input("Press Enter to return to home menu.")
    if score < 5:
        print(
            f'Yikes! Looks like you need some more practice\n{score}/10 is way too low, please try again!\n')
        input("Press Enter to return to home menu.")