''' CS_100 Mithun Manivannan
    HW_11 '''

def file_copy(in_file, out_file):
    inputFile = open(in_file, "r")
    outputFile = open(out_file, "w")
    for line in inputFile:
        outputFile.write(line)
    inputFile.close()
    outputFile.close()

def file_stats(in_file):
    inputFile = open(in_file, "r")
    numberOfLines = 0
    numberOfWords = 0
    numberOfChar = 0
    for line in inputFile:
        numberOfLines += 1
        lineList = line.split()
        for words in lineList:
            numberOfWords += 1
            for characters in words:
                numberOfChar += 1
    inputFile.close()
    print("lines:", numberOfLines)
    print("words:", numberOfWords)
    print("characters:", numberOfChar)

def repeat_words(inFile, outFile):
    import string
    inputFile = open(inFile, "r")
    outputFile = open(outFile, "w")
    for line in inputFile:
        lineList = []
        ListofLine = line.split()
        for word in ListofLine:
            if word not in lineList:
                lineList.append(lineList)
            else:
                word.lower()
                word.strip(string.punctuation)
                outputFile.write(newList)
    inputFile.close()
    outputFile.close()


                
