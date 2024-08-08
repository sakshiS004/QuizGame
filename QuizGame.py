
def new_game():

    ans = []
    correct_ans = 0
    question_num = 1

    for key in Question:
        print("\n")
        print(key)

        for i in Options[question_num - 1]:
            print(i)

        guess = input("\nEnter (A , B or C) : ").upper()
        ans.append(guess)
        correct_ans += check_ans(Question.get(key),guess)

        question_num += 1

    display_score(correct_ans,ans)

def check_ans(answer, guess):

    if answer == guess:
        print("CORRECT")
        return 1

    else:
        print("WRONG")
        return 0


def display_score(correct_ans, ans):
    print("\nRESULT\n")
    print("ANSWER: ", end="")
    for i in Question:
        print(Question.get(i), end=" ")

    print("\nGUESSES: ", end="")
    for i in ans:
        print(i, end=" ")

    score = int((correct_ans/len(Question))*100)
    print("\nYour total score is: "+str(score)+"%")


def play_again():
    response = input("Do you want to play again? (Y/N): ").upper()
    if response == "YES":
        return True
    else:
        return False


Question = {"Which planet is known as the 'Red Planet'?": "B",
            "Who wrote 'Romeo and Juliet'?": "C",
            "What is the process of a caterpillar changing into a butterfly called?":"A",
            "What is the chemical symbol for water?": "B",
            " Who invented the light bulb?": "C"
            }

Options = [["A. Mercury", "B. Mars", "C. Juptier"],
           ["A. Albert Einstein","B.Le o Tolstoy", "C. William Shakespeare"],
           ["A. Metamorphosis" , "B. Locomotion" , "C. Catadromus"],
           ["A. H2" , "B. H2O" , "C. H2O2"],
           ["A. Charles Babbage" , "B. Carl Benz ", "C. Thomas Edison"]]

new_game()

while play_again():
    new_game()

print("BYEEE !!")