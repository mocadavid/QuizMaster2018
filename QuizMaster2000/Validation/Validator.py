from NewExceptions.NewErrors import InvalidDifficulty


class ValidQuestion:

    pass

class ValidQuiz:

    def valid(self,object):
        diff=object.getDifficulty()
        if not diff is "easy" or diff is "medium" or diff is "hard":
            raise InvalidDifficulty("That is not a difficulty!")
        file=object.getFile()
        if not file in ".txt":
            raise InvalidFileFormat("This is not a .txt!")