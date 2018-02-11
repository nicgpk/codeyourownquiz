
easyQuiz = "There are ___1___ countries in the world. The countries with the biggest landmass is ___2___. The coldest continent in the world is ___3___. ___4___ is the capital of China"
easyAnswer = ["195","Russia","Antartica","Beijing"]

mediumQuiz = "___1___ has the largest trained military force in the world at 8,134,500 trained personel. Its neighbour ___2___ has the 2nd largest military force followed by ___3___ in the 3rd place with 5,522,000. Lastly in 4th place, ___4___ has 4,941,600 military personel."
mediumAnswer = ["South Korea","North Korea","Vietnam","India"]

hardQuiz = "Gross domestic product is also know as ___1___. It is derived from PPP calculations which is also called ___2___. The Richest Country in the world is ___3___, followed by Luxembourg at 2nd place and ___3___ in 3rd place."
hardAnswer = ["GDP","Purchasing Power Parity","Qatar","Singapore"]



blanks = ["___1___","___2___","___3___","___4___"]



#Introduction
print "Nic's Quiz"

#asks users to choose difficulty level
question = raw_input("Shall we start? Easy, Medium, Hard?")

def answerList(question):

    if question == "Easy" or question == "easy":
        return easyAnswer
    elif question == "Medium" or question == "medium":
        return mediumAnswer
    elif question == "Hard" or question == "hard":
        return hardAnswer

#funtion that defines difficulty level
def difficulty(question):
    """
    Input:
    Question that asks for difficulty
    Behavior:
    Prints the respective quiz based in input.
    Returns:
    Quiz level
    """

    #if input is not equal to these values asks them to try again with appropriate value.
    #while question != "Easy" or "easy" or "Medium" or "medium" or "Hard" or "hard":

    #if input equals value return the value

    if question == "Easy" or question == "easy":
        return easyQuiz

    elif question == "Medium" or question == "medium":
        return mediumQuiz

    elif question == "Hard" or question == "hard":
        return hardQuiz

    else:
        question = raw_input("Try Again, Please input only Easy, Medium, Hard! Thank you!")
    print difficulty

#function that goes through input answers
def answerQuestion():
    """
    Input:
    difficulty selected by users.
    Behavior:
    uses answers that relates to diffculty users suggest.
    loops through and see if answers are the same as the list of answers and prompt users.
    """

    #counts for answers in list
    answerCount = 0
    nextanswerCount = 1
    #counts for question number
    index = 1

    answerChoice = answerList(question)


    #if question number is less than amount of questions run the following coe
    while index < len(blanks) + 1:
        answer = raw_input("Please answer question " + str(index) + ":" +"\n")
        #if answer entered is not equal to the defined answers ask user to try again else notify them its the correct answer and go to the next question.
        while answer != answerChoice[answerCount]:
            answer = raw_input("Try Again!! Please answer with the first letter as a capital letter!")
        if answer == answerChoice[answerCount]:
            print "Please answer the next question!"
        replaceQuiz(replaceCount())
        index = index + 1
        answerCount = answerCount + 1
        nextanswerCount = nextanswerCount + 1

    correctanswer()

def replaceCount():
    count = 0
    while count < len(blanks):
        return count
        count = count + 1

def replaceQuiz(blankscount):

    answerChoice = answerList(question)
    newlist = []
    maxblank = 4

    for quizwords in difficulty(question).split():
        quizwords = quizwords.replace(blanks[blankscount],answerChoice[blankscount])

        newlist.append(quizwords)
        #print newlist


    joinedlist = " ".join(newlist)
    print joinedlist

def correctanswer():
    """
    Input:
    None.
    Behavior:
    Loops through answers and prints them out.
    Return:
    None
    """

    maxcount = 3

    answerCount = 0

    answerChoice = answerList(question)

    while answerCount < maxcount:
        print "Yes! The correct answers are"
        for answer in answerChoice:
            print answerChoice[answerCount]
            answerCount = answerCount + 1


#main funtion that calls the rest of the function
def main():
    """
    Input:
    None
    Behavior:
    Calls main functions used in this quiz
    Return:
    None
    """
    answerList(question)
    print difficulty(question)
    print answerQuestion()




main()
