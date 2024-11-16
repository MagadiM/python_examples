import random

questions = [
    {
        "question": "What does CSS stand for?",
        "options": ["A. Cascading Style Sheets", "B. Customizing Styling Sheets", "C. Cascading Styling Spread", "D. Custom style spreads"]
        "answer": "A"
    },
    {
        "question": "What does JSON stand for?",
        "options": ["A. JavaScript Object Number", "B. Java Styling Options", "C. Java Style Object Null", "D. JavaScript Object Notation"]
        "answer": "D"
    },
    {
        "question": "Is an array immutable or mutable?",
        "options": ["A. Immutable", "B. Mutable"]
        "answer": "B"
    },
    {
        "question": "What does a dictionary in python contain?",
        "options": ["A. object-method", "B. method-attribute", "C. Key-value", "D. key-chain"]
        "answer": "C"
    },
    {
        "question": "What do classes contain in python PL?",
        "options": ["A. object-key", "B. method-value", "C. Key-value", "D. class, object"]
        "answer": "D"
    }
]

def play_quizGame(question_list):
    print(question["question"])
    for option in question_list["options"]:
        print(option)
    player_answer = input("Enter your choice answer(A B C D): ".upper())
    if player_answer == question_list["answer"]:
        return True
    else: 
        return False 
