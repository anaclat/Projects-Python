from random import choice

def magic_8_ball():
    input('Ask your question to the Magic 8 Ball: ')

    answers = [
        "Absolutely!",
        "Without a doubt.",
        "Yes, definitely.",
        "Most likely.",
        "Outlook is good.",
        "Focus and ask again.",
        "Better not tell you now.",
        "Don't count on it.",
        "My sources say no.",
        "Very doubtful.",
        "The answer is complicated, try again later.",
        "I don't have an answer for that right now."
    ]

    print(choice(answers))