from random import randint


def talkingToBen():
    response = ""
    question = input("Ask a question: ")
    randomresponse = randint(1, 4)
    if (randomresponse == 1):
        response = "Yes"
    elif(randomresponse == 2):
        response = "No"
    elif(randomresponse == 3):
        response = "Hahahaha"
    else:
        response = "Ugh"
    print(f"You: \"{question}\"")
    print(f"Ben: \"{response}\"")


talkingToBen()
