from NewExceptions.NewErrors import InvalidCommand
from Texttable import texttable

class Console:

    def __init__(self,ctrlGame):
        self.ctrlGame = ctrlGame

    def mainMenuUI(self):
        commands={"add":self.ctrlGame.ctrlQuestion.addQuestion,"create":self.ctrlGame.ctrlQuiz.addQuiz}
        self.ctrlGame.ctrlQuestion.repo.loadFromFile()
        while True:
            try:
                answer=input(">")
                instruction=answer.split(";")
                directive=instruction[0].split(" ")
                if len(directive)<2:
                    raise InvalidCommand("Wrong Command!")
                idQuestion=int(directive[1])

                if directive[0] in commands:
                    commands[directive[0]](idQuestion,instruction[1],instruction[2],instruction[3],instruction[4],instruction[5],instruction[6])
                else:
                    raise InvalidCommand("Wrong Command!")

            except ValueError as ve:
                print(ve)
            except InvalidCommand as ic:
                print(ic)



