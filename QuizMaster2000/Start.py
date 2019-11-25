from Repository.TextRepo import TextRepo
from Service.Controller import CtrlHuman, CtrlGame, CtrlQuiz, CtrlQuestion
from UI.UserInput import Console
from Validation.Validator import ValidQuiz, ValidQuestion

repoQuiz=TextRepo()
validQuestion=ValidQuestion()
validQuiz=ValidQuiz()
serviceQuiz=CtrlQuiz(repoQuiz,validQuiz)
serviceQuestion=CtrlQuestion(repoQuiz,validQuestion)
serviceHuman=CtrlHuman()
serviceGame=CtrlGame(serviceQuiz,serviceQuestion,serviceHuman,validQuestion,validQuiz)
console=Console(serviceGame)

console.mainMenuUI()
