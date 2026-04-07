
print("Welcome to Jeopardy online")
print("The categories are science, history, python, pop culture, and movies")

science_questions = ["This organelle is famously known as the powerhouse of the cell", "Adults typically have between 206 and 213 of these in their bodies", "This iron-containing protein in red blood cells is responsible for carrying oxygen", "It is the largest organ in the human body", "This term describes a chemical reaction that releases energy into its surroundings"]
science_answers = ["mitochondria", "bones", "hemoglobin", "skin", "exothermic"]
history_questions = ["This ancient writing system, developed by the Sumerians, uses wedge-shaped marks on clay tablets", "In 1955, this woman famously refused to give up her bus seat in Montgomery, Alabama, sparking a major civil rights boycott", "She was the last active ruler of the Ptolemaic Kingdom of Egypt", "This Babylonian king is credited with creating one of the earliest and most complete written legal codes","This was the name of the first permanent English settlement in North America, founded in 1607"]
history_answers = ["cuneiform", "Rosa Parks", "Cleopatra", "Hammurabi", "Jamestown"]
python_questions = ["This keyword is used to define a new function in Python", "This built-in function allows you to capture text input from a user", "This common data structure is a collection of items referenced by a numeric index, defined with square brackets", " This statement is used to check a condition and create a branch in the code", "This keyword is used to immediately exit the current loop"]
python_answers = ["def", "input", "list", "if", "break"]
popculture_questions = ["This 2024 album by Charli XCX inspired a viral lime green summer aesthetic", " She holds the record for the most Grammy nominations in history with 88", "This singer performed the 2023 Super Bowl halftime show while pregnant", " Every episode of the sitcom Seinfeld famously contains a hidden reference to this superhero", "This is the name of the fictional town where Stranger Things takes place"]
popculture_answers = ["Brat", "Beyonce", "Rihanna", "Superman", "Hawkins"]
movies_questions = ["This is the name of the fictional city protected by Batman", "This African nation is the primary setting for the Black Panther films", "In Forrest Gump, he names his shrimp boat after this woman, his lifelong love.", "This 2019 South Korean film was the first non-English movie to win the Oscar for Best Picture", "This 2020 Christopher Nolan film follows a protagonist through inverted time"]
movies_answers = ["Gotham", "Wakanda", "Jenny", "Parasite", "Tenet"]
point_scores = [200, 400, 600, 800, 1000]

score = 0
bot_score = 0

while True:
    category = input("Choose a category")
    if category == "science":
        money = int(input("please enter a cash value of 200, 400, 800, or 1000 as a number:"))
        money_index = point_scores.index(money)
        question = science_questions[money_index]
        print(question)
        user_answer = input("answer(enter proper nouns with uppercase):")
        if user_answer == science_answers[money_index]:
            print("correct")
            score += money
        print(f"your score is ${score}")
        stop = input("please enter stop if you would like to stop. if not enter no.")
        if stop == "stop":
            break
    elif category == "history":
        money = int(input("please enter a cash value of 200, 400, 800, or 1000 as a number:"))
        money_index = point_scores.index(money)
        question = history_questions[money_index]
        print(question)
        user_answer = input("answer(enter proper nouns with uppercase):")
        if user_answer == history_answers[money_index]:
            print("correct")
            score += money
        print(f"your score is ${score}")
        stop = input("please enter stop if you would like to stop. if not enter no.")
        if stop == "stop":
            break
    elif category == "python":
        money = int(input("please enter a cash value of 200, 400, 800, or 1000 as a number:"))
        money_index = point_scores.index(money)
        question = python_questions[money_index]
        print(question)
        user_answer = input("answer(enter proper nouns with uppercase):")
        if user_answer == python_answers[money_index]:
            print("correct")
            score += money
        print(f"your score is ${score}")
        stop = input("please enter stop if you would like to stop. if not enter no.")
        if stop == "stop":
            break
    elif category == "pop culture":
        money = int(input("please enter a cash value of 200, 400, 800, or 1000 as a number:"))
        money_index = point_scores.index(money)
        question = popculture_questions[money_index]
        print(question)
        user_answer = input("answer(enter proper nouns with uppercase):")
        if user_answer == popculture_answers[money_index]:
            print("correct")
            score += money
        print(f"your score is ${score}")
        stop = input("please enter stop if you would like to stop. if not enter no.")
        if stop == "stop":
            break
    elif category == "movies":
        money = int(input("please enter a cash value of 200, 400, 800, or 1000 as a number:"))
        money_index = point_scores.index(money)
        question = movies_answers[money_index]
        print(question)
        user_answer = input("answer(enter proper nouns with uppercase):")
        if user_answer == movies_questions[money_index]:
            print("correct")
            score += money
        else:
            print("incorect")
            bot_score += money
        print(f"your score is ${score}")
        stop = input("please enter stop if you would like to stop. if not enter no.")
        if stop == "stop":
            break
    else:
        print("please enter a valid category")

print(f"your score is ${score} and enemy score is {bot_score}.")
if score > bot_score:
    print("you won!!")
elif score == bot_score:
    print("you tied.")
else:
    print("sorry you lost.")