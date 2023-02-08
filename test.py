from BitVector import *
def getAllPossibleWords(length):
    from english_words import get_english_words_set
    wordList = []
    wordSet = get_english_words_set(['web2'])
    for x in wordSet:
        if len(x) == length:
            wordList.append(x)
    return wordList

def getBitvectorOfEncryptedText():
    encryptWords = []
    BitVectors = []
    with open ("input.txt", "r") as myfile:
        encryptWords = myfile.read().splitlines()
    firstEncryptWord = encryptWords[0].strip().replace(" ", "")
    secondEncryptWord = encryptWords[1].strip().replace(" ", "")
    BitVectors.append(BitVector(hexstring  =firstEncryptWord))
    BitVectors.append(BitVector(hexstring  =secondEncryptWord))
    return BitVectors

    
allWords = getAllPossibleWords(8)
encryptedTextBitVectors = getBitvectorOfEncryptedText()
finalans = []
isFound = False
for x in range(0,len(allWords)-1):
    print(x)
    bv1 = BitVector(textstring  = allWords[x])
    temp = bv1^encryptedTextBitVectors[0]
    for y in range(x,len(allWords)):     
        bv2 = BitVector(textstring  = allWords[y])
        if temp==bv2^encryptedTextBitVectors[1]:
            finalans.append(allWords[x])
            finalans.append(allWords[y])
            isFound = True
            break
    if isFound == True:
        break
   
if isFound == False:
    print("NO words found")
else:
    with open ("output.txt", "w") as myfile:
                myfile.write(str(finalans))
           
        