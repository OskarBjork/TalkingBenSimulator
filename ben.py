from random import random


def talkingToBen():
    response = ""
    question = input("Ask a question: ")
    randomresponse = random
    if (randomresponse == 0):
        response = "Yes"
    else:
        response = "No"
    print(f"You: \"{question}\"")
    print(f"Ben: \"{response}\"")


talkingToBen()
