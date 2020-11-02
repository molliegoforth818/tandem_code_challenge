
def correct():
    print("THATS RIGHT!")
    input("Press Enter to go to next question.")



def incorrect(question_object):
    print("WRONG!")
    print(question_object['correct'], 'is the correct answer.\n\n')
    input("Press Enter to go to next question.")


