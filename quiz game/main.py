





name = input('''Enter your name to take this test
''')
print(f"{name} you have 1 minute to complete this test")
from biology_questions import  bio_quiz
from biology_answers import bio_ans

score = 0
	
for i in range(len(questions)):
    while True:
        ans = input(questions[i]).strip().lower()
        if ans in ["a", "b", "c", "d"]:
            break
    else:
        print('''Please enter any of the given options only''')
    if ans == answers[i]:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
        print(explaination[i])
        print(f"Biology test completed. You scored {score}/{len(questions)}")

from physics_questions import phy_quiz
from physics_answers import phy_ans
score = 0
    
for i in range(len(questions)):
    while True:
        ans = input(questions[i]).strip().lower()
        if ans in ["a", "b", "c", "d"]:
            break
        else:
            print("Please enter any of the given options only")
        if ans == answers[i]:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
            print(explaination[i])
        print(f"Physics test completed. You scored {score}/{len(questions)}")
        bio_score, bio_questions = bio_quiz()
        phy_score, phy_questions = phy_quiz()
        total_score = bio_score + phy_score
        total_questions = bio_questions + phy_questions
        Percentage = (total_score/total_questions)*100
        print(f'''
Dear {name},
Your total score is: {total_score}
Percentage: {Percentage}%''')
if Percentage < 50:
 print('''That's pathetic
 
 ''')
if Percentage >= 50 and Percentage <= 70:
 print('''Unsatisfactory. I expected better
 
 ''')
if Percentage > 70 and Percentage < 100:
 print('''A bit good
 
 ''')
if Percentage == 100:
 print('''I am very proud of you.
 
 ''')