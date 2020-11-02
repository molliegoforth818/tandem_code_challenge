import random

def get_answer_list(question_object):
    answers = []  #creating empty list to interate thru the list of answers
    answers.append(question_object['correct'])
    for answer in question_object['incorrect']:
        answers.append(answer)
    random.shuffle(answers)  #shuffling answer so that d isn't the correct answer everytime
    return answers


def show_answers(answers):
    for index, a in enumerate(answers):
        print(f'{index + 1}. {a}')

