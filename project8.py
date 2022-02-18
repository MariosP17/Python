import random
def chess(h,w):
    position= []
    bwins = []
    wwins = []
    for x in range(1,h+1):
        for y in range(1,w+1):
            position.append((x,y))
    for n in range(100):
        wRook = random.choice(position)
        bBishop = random.choice(position)
        while wRook == bBishop:
         bBishop = random.choice(position)
        print(str(n+1)+")",'Πύργος:',wRook,'Αξιωματικός:',bBishop)
        rookX, rookY = wRook
        bishopX, bishopY = bBishop
        if rookX == bishopX or rookY == bishopY:
            wwins.append(n+1)
        if (rookX - bishopX == rookY - bishopY):
            bwins.append(n+1)
        elif (-rookX + bishopX == rookY - bishopY):
            bwins.append(n+1)
    white , black , roundw , roundb = len(wwins), len(bwins), str(wwins)[1:-1] , str(bwins)[1:-1] 
    print('Σε εκατό γύρους πάνω σε σκακιέρα διαστάσεων '+str(h)+'*'+str(w)+' ο παίκτης με τον λευκό πύργο νίκησε',white,'φορές στους γύρους:',roundw,'και ο παίκτης με τον μαύρο αξιωματικό νίκησε',black,'φορές στους γύρους:',roundb)
    print(" ")
chess(8,8)
chess(7,7)
chess(7,8)
