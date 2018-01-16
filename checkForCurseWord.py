from urllib import request

def readTxt():
    """read any text file from a location"""
    openFileToread=open(r"D:\Akshay\repoOATS\pythonRepo\checkTheword.txt")
    readContent=openFileToread.read()
    print (readContent)
    openFileToread.close()
    checkProfanity(readContent)


def checkProfanity(textToCheck):
    """open an url """
    #connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+textToCheck)

    connection=request.urlopen("http://www.wdylike.appspot.com/?q="+textToCheck)
    """check the output from the connection opened"""
    output=connection.read()
    #print output
    if "true" in output:
        print ("has curse words")
    else:
        print ("your text is ok")


def checkWhatAWebPageReturns():
    connectionNew=urllib.urlopen("www.google.co.in")
    outputOfURL=connectionNew.read()
    print (outputOfURL)

readTxt()
#checkWhatAWebPageReturns()