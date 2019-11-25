from Model.Entities import Question, Quiz
from NewExceptions.NewErrors import InvalidCommand


class CtrlGame:

    def __init__(self,ctrlQuiz,ctrlQuestion,ctrlHuman,validQuestion,validQuiz):
        self.validQuiz = validQuiz
        self.validQuestion = validQuestion
        self.ctrlHuman = ctrlHuman
        self.ctrlQuestion = ctrlQuestion
        self.ctrlQuiz = ctrlQuiz


class CtrlHuman:

    def __init__(self):
        pass

class CtrlQuestion:

    def __init__(self,repo,valid):
        self.valid = valid
        self.repo = repo

    def addQuestion(self,id,instruction):
        #text,a,b,c,correct,difficulty
        if len(instruction) < 7 or len(instruction) > 7:
            raise InvalidCommand("Wrong Command!")
        #text=

        #question1=Question(id,text,a,b,c,correct,difficulty)
        #self.repo.add(id,question1)


class CtrlQuiz:

    def __init__(self,repo,valid):
        self.valid = valid
        self.repo = repo

    def addQuiz(self,difficulty,number,file):
        quiz1=Quiz(difficulty,number,file)
        self.valid.valid(quiz1)
        self.storeQuiz()

    def storeQuiz(self):
        pass


