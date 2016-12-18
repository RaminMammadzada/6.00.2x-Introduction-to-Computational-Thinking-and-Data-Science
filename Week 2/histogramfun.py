import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    # MY CODE
    vowel_proportions=[]
    for word in wordList:
        num=0
        for letter in word:
            if letter in 'aeiou':
                num=num+1
        vowel_proportions.append(num/float(len(word)))

    greater=0
    less=0
    for prop in vowel_proportions:
        if prop>0.5:
            greater+=1
        elif prop<0.5:
            less+=1

    print 'greater: ', greater
    print 'less: ', less
    pylab.hist(vowel_proportions, numBins)
    pylab.figure()
    # MY CODE

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
