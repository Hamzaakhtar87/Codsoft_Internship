import random

questions = [
    {
        "question": "What gas do plants primarily use for photosynthesis?",
        "choices": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
        "correct_answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "choices": ["A. Mark Twain", "B. William Shakespeare", "C. J.K. Rowling", "D. George Orwell"],
        "correct_answer": "B"
    },
    {
        "question": "What is the largest mammal on Earth?",
        "choices": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Polar Bear"],
        "correct_answer": "B"
    },
    {
        "question": "What is the chemical symbol for the element gold?",
        "choices": ["A. Go", "B. Gd", "C. Au", "D. Ag"],
        "correct_answer": "C"
    },
    {
        "question": "What is the process by which plants make their own food called?",
        "answer": "Photosynthesis"
    },
    {
        "question": "Which famous scientist developed the theory of relativity?",
        "answer": "Albert Einstein"
    },
    {
    "question": "Which planet is known as the 'Morning Star'?",
    "choices": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    "correct_answer": "A"
    },
    {
        "question": "What is the capital of France?",
        "choices": ["A. London", "B. Paris", "C. Rome", "D. Madrid"],
        "correct_answer": "B"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "choices": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "correct_answer": "B"
    },
    {
        "question": "The Earth revolves around the _____.",
        "answer": "Sun"
    }
]
score = 0

def display_welcome():
    print("\n     Welcome to the Quiz Game!       \n")

def ask_question(question_data):
    print(question_data["question"])

    if "choices" in question_data:
        for choice in question_data["choices"]:
            print(choice)
        user_answer = input("\nEnter Your choice A\B\C\D or type 'Quit' to End the Quiz: ")
    else:
        user_answer = input("\nEnter Your Answer or Type 'Quit' to End the Quiz: ")

    return user_answer

def check_answer(question_data, user_answer):
    global score

    if "choices" in question_data:
        if user_answer.upper() == question_data["correct_answer"].upper():
            score += 1
            print("\nCorrect Answer\n")
            print("You Got 1 score, your score is: ", score)
        else:
            print("Wrong Answer")
            print("Correct Answer is: ", question_data["correct_answer"])
    else:
        if user_answer.lower() == question_data["answer"].lower():
            print("Correct Answer")
            score += 1
            print("You Got 1 score, your score is: ", score)
        else:
            print("Wrong Answer")
            print("Correct Answer is: ", question_data["answer"])

random.shuffle(questions)

display_welcome()
for question in questions:
    user_choice = ask_question(question)
    if user_choice.lower() == "quit":
        break
    check_answer(question, user_choice)
    print("_" * 40, "\n")

print(f"Quiz Ended, Your total score is: {score}")

if score >= 5:
    print("Congratulations, You Passes the Quiz")
else:
    print("You Failed the Quiz!")
