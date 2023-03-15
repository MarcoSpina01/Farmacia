from os.path import abspath

class Gestore:

    def returnPth(self):
        abp = abspath("iconacarrello.PNG")
        split = [abp.split("\\")]
        pthArr = []
        finPth = ""

        for element in split:
            if element == split[len(split) - 1]:
                pthArr += element

        for x in range(5):
            finPth += str(pthArr[x]) + "/"
        return finPth