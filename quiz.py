from quiz_questions import questions
import os


def ask(questions):
    end_of_game = False
    correct = ""
    score = 0
    qes = []
    opt = ""
    while end_of_game == False:
        for question in questions:
            value_ques = questions[question]

            for e, i in enumerate(value_ques):
                if len(i) == 1:
                    opt += i
                    continue
                if "c" == i[0]:
                    correct += i[1::]
                    qes.append(f"{i[1::]}")
                else:
                    if e == 1:
                        qes.append(f"{i}")
                    else:
                        qes.append(f"{i}")
            for j in qes:
                #print(f"Your current score: {score}")
                userans = input(f"{question}: \nA: {qes[0]} \nB: {qes[1]} \nC: {qes[2]} \nD: {qes[3]} \nans: ").upper()
                print()
                if userans == opt:
                    score+=1
                    print("Correct Answer")
                    questions.pop(question)
                    ask(questions)
                else:
                    if questions == {}:
                        print("Your done with questions")
                    os.system('cls')
                    go_again = input("Wrong answer, Type 'yes' to try again or 'no': ").lower()
                    
                if go_again == 'no':
                    end_of_game = True
                    break
            break
ask(questions)
