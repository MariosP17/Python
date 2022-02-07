import math
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(bin(i)[2:])
  return m
def changeToBin(a):
    f = open(a, 'r+')
    read=f.read()
    Bin = toBinary(read)
    with open(a, 'w+') as result:
         result.writelines(Bin[i]+' ' for i in range(len(Bin)))
    f.close()
def readBin(a):
    f = open(a, 'r+')
    read = f.read()
    new = read.split(' ')
    new.pop()
    if any("11" in s for s in new):
     num = 2
    if any("111" in s for s in new):
     num = 3 
    if any("1111" in s for s in new):
     num = 4
    if any("11111" in s for s in new):
     num = 5
    if any("111111" in s for s in new):
     num = 6
    if any("1111111" in s for s in new):
     num = 7
    if any("00" in s for s in new):
     num0 = 2
    if any("000" in s for s in new):
     num0 = 3 
    if any("0000" in s for s in new):
     num0 = 4
    if any("00000" in s for s in new):
     num0 = 5
    if any("000000" in s for s in new):
     num0 = 6
    if any("0000000" in s for s in new):
     num0 = 7
    print("Η μεγαλύτερη ακολουθία από 1 είναι " + str(num) + " άσσοι!")
    print("Η μεγαλύτερη ακολουθία από 0 είναι " + str(num0) + " μηδενικά!")
    f.close()
changeToBin('text.txt')
readBin("text.txt")