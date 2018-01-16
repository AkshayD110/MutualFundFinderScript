import codecs
import xlrd
import collections
import unicodedata


def readFundbook(path):
    fundBook=xlrd.open_workbook(path)
    numberOfSheets=fundBook.nsheets
    iterator=0
    listOfFunds = []
    finalListOfFunds = []

    while(iterator<numberOfSheets):
        #listOfFunds.append(fundBook.sheet_by_index(iterator).col_values(0))
        """gets the current sheet and prints its name"""
        currentSheet=fundBook.sheet_by_index(iterator)
        #print currentSheet.name

        """gets the number of columns and rows in the sheet"""
        noColms=currentSheet.ncols
        noRows=currentSheet.nrows
        #print noRows, noColms

        """iterates through all the columns and appending  the values"""
        for row_idx in range(0, noRows):
            cellObject=currentSheet.cell(row_idx, 0)
            cellObject=str(cellObject)
            cellObject=cellObject[6:]
            listOfFunds.append(cellObject)

        iterator=iterator+1
        #print (fundBook.sheet_by_index(iterator).nrows)

    #print (len(listOfFunds))
    #print listOfFunds
    #print (len(listOfFunds))
    #print listOfFunds
    """below loop not required, as it is taken care of in the above loop"""
    """this listOfFunds list has unicodes in its values. Iterate through it, and convert all values to str, and add to another list"""
    #for allFunds in listOfFunds:
        #print allFunds
     #   thisFund=allFunds
      #  thisFund=str(thisFund) #important to convert it to str from cell type to do collection.counter operation next
       # thisFund=thisFund[6:] #slicing the data to remove the unicode values
        #look more in to how slicing works
        #https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation
        #finalListOfFunds.append(thisFund) #final list which will have all the fund names in string format

    """gets the count of number of times a fund was suggest. Counts the number of times an element was repeated"""
    listOfFunds = filter(lambda a: a !='Funds\'', listOfFunds) #removes the first column, "Funds" from the list count
    frequency=collections.Counter(listOfFunds)
    #print frequency
    print ("Below funds have been suggested out of " + str(numberOfSheets) + " iterations")
    print (frequency.most_common()) #sorts the collection by values

    #print (frequency.values())
    #print finalListOfFunds
    #print type(finalListOfFunds)


def checkConcent():
    a=["a","a","b","e","f","t","y","a","b"]
    freqConcept=collections.Counter(a)
    print (a)
    print (freqConcept)


readFundbook(r"C:\Users\akshdesh.ORADEV\Documents\money\OnlyFund.xlsx")
#checkConcent()