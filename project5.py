import re
def makeLower (str):
    f = open(str, 'r+')
    low = [line.lower() for line in f]
    with open(str, 'w+') as result:
        result.writelines(low)
    f.close()
def removeNonLetter(str):
    f = open(str, 'r+')
    read = f.read()
    regex = re.compile('[^a-zA-Z]')
    replace = regex.sub(' ', read)
    final = re.sub(' +',' ', replace)
    with open(str, 'w+') as result:
        result.writelines(final)
    f.close()
def countWords(a):
    from collections import Counter
    f = open(a, 'r+')
    read = f.read()
    list = read.split(' ')
    Counter = Counter(list)
    mostCommon = Counter.most_common(10)
    print('Oι δέκα πιο δημοφιλείς λέξεις με την συχνότητα τους ειναι: '+ str(mostCommon))
    f.close  
def countDoubles(a):
    listOfTwo = []
    from collections import Counter
    f = open(a, 'r+')
    read = f.read()
    list = read.split(' ')
    for s in list:
        if len(s)>2:
         listOfTwo.append(s[:2])
    Counter = Counter(listOfTwo)
    mostCommon = Counter.most_common(3)
    print('Oι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις με την συχνότητα τους ειναι: '+ str(mostCommon))
    f.close  
def countTriples(a):
    listOfThree = []
    from collections import Counter
    f = open(a, 'r+')
    read = f.read()
    list = read.split(' ')
    num = len(list)
    for s in list:
        if len(s)>3:
         listOfThree.append(s[:3])
    Counter = Counter(listOfThree)
    mostCommon = Counter.most_common(3)
    print('Oι τρεις πρώτοι συνδυασμοί τριών πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις με την συχνότητα τους ειναι: ' + str(mostCommon))
    f.close  
makeLower("text.txt")    
removeNonLetter("text.txt")
countWords("text.txt")
countDoubles("text.txt")
countTriples("text.txt")
