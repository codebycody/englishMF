# Detect English
# To use, type this code:
#   import englishMF
#   englishMF.isEnglish(something) # Returns True or False
#  
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('EN.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word.upper()] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()


def getEnglishCount(msg):
    msg = msg.upper()
    msg = removeNonLetters(msg)
    possibleWords = msg.split()

    if possibleWords == []:
        return 0.0 # No words at all, returning 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def removeNonLetters(msg):
    lettersOnly = []
    for symbol in msg:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglish(msg, wordPercentage=20, letterPercentage=85):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    wordsMatch = getEnglishCount(msg) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(msg))
    messageLettersPercentage = float(numLetters) / len(msg) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch