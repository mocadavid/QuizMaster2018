from Model.Entities import Question


class TextRepo:

    def __init__(self):
        self.__dict={}
        self.__fileStorage="masterquestionlist.txt"

    def loadFromFile(self):
        file=open(self.__fileStorage,"r")
        rawlines=file.readlines()
        for rawline in rawlines:
            lines=rawline.split(";")
            object=Question(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6])
            id=int(lines[0])
            self.add(id,object)
        file.close()


    def add(self,id,object):
        #
        self.__dict[id]=object
        self.saveToFile()

    def getAll(self):
        return list(self.__dict.values())

    def saveToFile(self):
        file=open("test.txt","w")
        #self.__fileStorage
        for object in self.getAll():
            file.write(object.questionToFile())
            file.write("\n")
        file.close()

