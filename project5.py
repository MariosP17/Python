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
    def firstTwo(s):
        return s[:2]
    from collections import Counter
    f = open(a, 'r+')
    read = f.read()
    list = read.split(' ')
    num = len(list)
    for i in range(num):
       if len(list[i]) == 2:
           listOfTwo.append(list[i])
    Counter = Counter(listOfTwo)
    mostCommon = Counter.most_common(3)
    print('Oι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις με την συχνότητα τους ειναι: '+ str(mostCommon))
    f.close  
def countTriples(a):
    listOfThree = []
    def firstThree(s):
        return s[:3]
    from collections import Counter
    f = open(a, 'r+')
    read = f.read()
    list = read.split(' ')
    num = len(list)
    for i in range(num):
       if len(list[i]) == 3:
           listOfThree.append(list[i])
    Counter = Counter(listOfThree)
    mostCommon = Counter.most_common(3)
    print('Oι τρεις πρώτοι συνδυασμοί τριών πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις με την συχνότητα τους ειναι: ' + str(mostCommon))
    f.close  
makeLower("text.txt")    
removeNonLetter("text.txt")
countWords("text.txt")
countDoubles("text.txt")
countTriples("text.txt")
