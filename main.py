#Quiz
#Tim Nguyen
#02/08/22

def main():
    import time
    
    #Introcution, welcome message
    print("Welcome to my quiz")
    print("Every question you get right that adds 1 to your score")
    time.sleep(1)
    print("Every question you get wrong subtracts 1 from your score")
    time.sleep(1)

    score = 0

    #Question
    question_1 = input("When was Python created? ")
    #Answer
    answer_1 = "1991"

    if question_1 == answer_1:
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")
        score = score - 1

    time.sleep(1)

    #Question
    question_2 = input("True or False? Guido van Rossum created Python ").lower()
    #Answer
    answer_2 = "true"


    if question_2 == answer_2:
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")
        score = score - 1
    time.sleep(1)
    
    #Display final result to answer
    print("Your final score was", score)

    replay = input("Would you like to play again? ").lower()
    if replay == "yes":
        main()
    else:
        #Ending message
        print("Thank you for playing")
    

main()

