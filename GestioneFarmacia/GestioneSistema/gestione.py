from os.path import abspath

class Gestore:

    def returnPth(self):
        abp = abspath("")
        split = [abp.split("\\")]
        pthArr = []
        finPth = ""

        for element in split:
            if element == split[len(split) - 1]:
                pthArr += element
        for x in range(len(pthArr)-1):
            finPth += str(pthArr[x]) + "/"

        return finPth