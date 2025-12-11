import random


def welcome():
    print("Hello, Welcome to the Comicon Trivia Game")
    print("What do you like to do?")

    print("1. Marvel")
    print("2. DC")

    while True:
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                marvel_trivia()
                break
            case "2":
                dc_trivia()
                break
            case "_":
                continue


# prepare questions and answers
marvel_questions ={
        "What metal is Wolverine's skeleton bonded with?": "Adamantium",
        "Which Avenger is known as the 'God of Thunder'?": "Thor",
        "Who is the strongest avenger ?": "Hulk",
        "What Infinity Stone is purple?": "Power",
        "Who is Tony Stark’s AI assistant after JARVIS?": "Friday",
        "Who is the Winter Soldier?": "Bucky",
        "Which hero uses the shield made of Vibranium?": "Captain America",
        "Who is the main villain in Avengers: Endgame?": "Thanos",
        "Which Avenger is known as the 'Scarlet Witch'?": "Wanda",
        "Who leads the Ravagers before Star-Lord?": "Yondu"
    }

dc_questions = {
    "Who is known as the Dark Knight?": "Batman",
    "What is Superman’s home planet?": "Krypton",
    "Who is the Amazonian princess superhero?": "Wonder Woman",
    "What is the name of Aquaman's underwater kingdom?": "Atlantis",
    "Which villain is known as the Clown Prince of Crime?": "Joker",
    "Who is the fastest man alive?": "Flash",
    "What power source fuels Green Lantern's ring?": "Willpower",
    "Which villain is known for using riddles?": "Riddler",
    "Who is the king of Apokolips?": "Darkseid",
    "Which hero is half-man, half-machine?": "Cyborg"
}

def marvel_trivia():

    marvel_question = list(marvel_questions.keys())

    total_questions = 5
    score=0

    # Chooses k unique random elements from a population sequence.
    # Returns a    new   list containing elements  from the population while leaving the original population unchanged.

    random_questions = random.sample(marvel_question, total_questions)
    # print(selected_question)

    """
    print question and get the answer
    check if it correct
    add score count
    """
    for index,question in enumerate(random_questions):
        print(f"\nQuestion {index+1} ", end="")
        user_answer = input(f"{question}: ").title().strip()

        correct_answer = marvel_questions[question]

        if user_answer == correct_answer.title():
            print(f"Correct!\n")
            score+=1
        else:
            print(f"Incorrect!.The Correct answer is: {correct_answer}.\n")

    print(f"You got {score} out of {total_questions} questions.")


def dc_trivia():
    dc_question = list(dc_questions.keys())

    total_questions = 5
    score=0

    random_questions = random.sample(dc_question, total_questions)

    for index,question in enumerate(random_questions):
        print(f"\nQuestion {index+1} ", end="")
        user_answer = input(f"{question}: ").title().strip()

        correct_answer = dc_questions[question]

        if user_answer == correct_answer.title():
            print(f"Correct!\n")
            score+=1
        else:
            print(f"Incorrect!.The Correct answer is: {correct_answer}.\n")

    print(f"You got {score} out of {total_questions} questions.")


    #  Replace Recursion in main for clean algorithm

"""
def main():
    welcome()

    print("\n\n")

    while True:
        re_attempt=input("Enter N to quit and Enter Y to another session:").upper()

        if re_attempt == "N":
            print("Good Bye")
            exit()
        elif re_attempt == "Y":
            main()
        else:
            print("Please enter a correct letter.")
"""


def main():
    while True:
        welcome()
        print("\n")

        re_attempt = input("Enter N to quit or Y for another session: ").upper()

        if re_attempt == "N":
            print("Good Bye")
            break
        elif re_attempt == "Y":
            continue
        else:
            print("Please enter a correct letter.\n")


if __name__ == '__main__':
    main()