from biology_questions import bio_questions
from biology_answers import biology_answers,bio_explanations as explanation
from physics_questions import physics_questions
from physics_answers import physics_answers,phy_explanations as explanation1



name = input("Enter your name to take this test\n")
print(f"{name} you have 10 minutes to complete this test")
print("Section 1: Biology Quiz \n Attempt all questions.\n")

bio_score = 0
	
for i in range(len(bio_questions)):
    while True:
        ans = input(bio_questions[i]).strip().lower()
        if ans in ["a", "b", "c", "d"]:
            break
        else:
            print("Please enter any of the given options only")


    if ans == biology_answers[i]:
        print("Correct!\n")
        bio_score += 1
    else:
        print("Incorrect!\n")
        print(explanation[i])
        print()
print(f"Biology test completed. You scored {bio_score}/{len(bio_questions)}\n")

#physics quiz
print("Section 2. Physics test; \n Answer all questions")
phy_score = 0
    
for i in range(len(physics_questions)):
    while True:
        ans = input(physics_questions[i]).strip().lower()
        if ans in ["a", "b", "c", "d"]:
            break
        else:
            print("Please enter any of the given options (a,b,c,d) only.")
    if ans == physics_answers[i]:
            print("Correct!\n")
            phy_score += 1
    else:
            print("Incorrect!\n")
            print(explanation1[i])
print(f"Physics test completed. You scored {phy_score}/{len(physics_questions)}\n")

#total results
       
total_score = bio_score + phy_score
total_questions = len(bio_questions) + len(physics_questions)
Percentage = (total_score/total_questions)*100
print(f'''
Dear {name},
Your total score is: {total_score}/{total_questions}
Percentage: {Percentage}%''')


if Percentage < 50:
    print("That's pathetic\n")

if Percentage >= 50 and Percentage <= 70:
    print("Unsatisfactory. I expected better\n")
if Percentage > 70 and Percentage < 100:
    print("A bit good\n")
if Percentage == 100:
    print("I am very proud of you.\n")