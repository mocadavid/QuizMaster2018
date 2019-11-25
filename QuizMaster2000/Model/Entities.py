class Question:

    def __init__(self,id,text,a,b,c,correct,difficulty):
        self.__difficulty = difficulty
        self.__correct = correct
        self.__c = c
        self.__b = b
        self.__a = a
        self.__text = text
        self.__id = id

    def getId(self):
        return self.__id

    def getText(self):
        return self.__text

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getCorrect(self):
        return self.__correct

    def getDifficulty(self):
        return self.__difficulty

    def questionToFile(self):
        return str(self.__id)+";"+self.__text+";"+self.__a+";"+self.__b+";"+self.__c+";"+self.__correct+";"+self.__difficulty

    def questionToStr(self):
        return self.__text+"\n"+"a. "+self.__a+" b. "+self.__b+" c. "+self.__c

class Quiz:

    def __init__(self,difficuty,number,file):
        self.__file = file
        self.__number = number
        self.__difficuty = difficuty

    def getDifficulty(self):
        return self.__difficuty

    def getFile(self):
        return self.__file




