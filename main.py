def printbook():
    with open("github.com/bscarman/bookbot/books/frankenstein.txt") as f:
    # ...
        file_contents = f.read()
        print (file_contents)

def countWords():
    with open("github.com/bscarman/bookbot/books/frankenstein.txt") as f:
    # ...
        file_contents = f.read()
        words = file_contents.split()
        
        #print(len(words))
        return(len(words))

def countLetters():
     with open("github.com/bscarman/bookbot/books/frankenstein.txt") as f:
        # prepare text
        file_contents = f.read()
        lowered_string = file_contents.lower()
        letterDictionary = {} 
        count=0
        # analyse text
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters :
            count = lowered_string.count(letter)
            letterDictionary[letter] = count
        return(letterDictionary)
     
def writeReport():
    numberOfWords = countWords()
    letterDictionary = countLetters()
    letterList = []
    letterList.append(letterDictionary) 
    sortedList = sorted(letterDictionary.items(), key=lambda x: x[1], reverse=True) 
    listOfReportLines = []
    print("listagain",sortedList)
    # Report building
    reportOnWordsString= (numberOfWords,)
    listOfReportLines.append("--- Begin report of books/frankenstein.txt ---")
    listOfReportLines.append(str(numberOfWords)+ " words found in the document")
    listOfReportLines.append('')
    for x in sortedList:
        listOfReportLines.append("The '"+ str(x[0])+ "' character was found "+ str(x[1])+" times")
    for x in listOfReportLines:
        print(x)    

if __name__ == "__main__":
    #main()
    #printbook()
    #countWords()
    #countLetters()
    writeReport()



