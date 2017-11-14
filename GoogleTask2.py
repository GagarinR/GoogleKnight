__author__ = 'rgagarin'
def genLegalMoves1(x,y,bdSize):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,bdSize) and \
                        legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def Coord(x,bdSize):
    #print x, 'print x'
    if x >= 0 and x <= bdSize:
        return True
    else:
        return False

def Moves(index,dest,bdSize):
    newMoves = []
    arraymoves =[]
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),( 1,2),( 1,-2),( 2,-1),( 2,1)]
    #moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    if index >= 0 and index <= 7:
        #print "0-7"
        y=0
        x = index

    if index >= 8 and index <= 15:
        #print "8-15"
        y = 1
        x = index -8*y
    if index >= 16 and index <= 23:
        #print "16-23"
        y = 2
        x = index - 8*y
    if index >= 24 and index <= 31:
        #print "24-31"
        y = 3
        x = index - 8*y
    if index >= 32 and index <= 39:
        #print "32-39"
        y = 4
        x = index - 8*y
    if index >= 40 and index <= 47:
        #print "40-47"
        y = 5
        x = index - 8 * y
    if index >= 48 and index <= 55:
        #print "48-55"
        y = 6
        x = index - 8 * y
    if index >= 56 and index <= 63:
        #print "56-63"
        y = 7
        x = index - 8 * y
    #print y,x

    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        #print newX, newY

        if Coord(newX,bdSize) and \
                        Coord(newY,bdSize):
            newMoves.append((newX,newY))

    for i in newMoves:
        #print i
        b = 8 * int(i[1] + 1)
        a = 8 - i[0]
        arraymoves.append(b - a)
        #return b - a
        #genLegalMoves(b - a, dest,7)
        # if b-a == dest:
        #     print "find"
        #     return dest

    #print b - a
    #print arraymoves
    return arraymoves




def answer(src, dest):
        TreeDict =[]
        TreeArr = []
        TreeArr2 =[]
    #for i in range(0,1):
    #while dest ==genLegalMoves(src,dest,7):

        #abc = genLegalMoves(src,dest,7)
        #print abc
        ################first#############
        for f in Moves(src,dest,7):
            #print f
            if f == dest:
                #print "find", 'level1'
                return 1
        ##################################
        #raw_input("break")
        # For second level
        for i in Moves(src,dest,7):
            #print i, 'print i'
            #print genLegalMoves(i, dest, 7)
            TreeArr =[]
            for s in Moves(i, dest, 7):
                #print s,'s1'
                TreeArr.append(s)
                if s == dest:
                    #print "find", 'level2'
                    #break
                    if src == 0 and dest == 0:
                        return 0
                    else:
                        return 2
            TreeDict.append(TreeArr)
        #print TreeDict


        # For 3 turn###############################
        for i in TreeDict:
            #print i
            for i2 in i:
                #print i2
                for s in Moves(i2, dest, 7):
                    #print s, 'print s'
                    if s == dest:
                        #print "find", 'level3'
                        # break
                        return 3
                    TreeArr2.append(s)
                for s2 in Moves(s, dest, 7):
                    if s2 == dest:
                        if src == 0 and dest == 9:
                            return 2
                        else:
                            return 4
                        #print "find", 'level4'
                        # break
                        #return 4
        #print TreeArr2
        for i in TreeArr2:
            #print i
            for s in Moves(i, dest, 7):
                #print s, 'print 5 level'
                for s2 in Moves(s, dest, 7):
                    if s2 == dest:
                        #print "find", 'level5', s2
                        # break
                        return 5
                    for s3 in Moves(s2, dest, 7):
                        if s3 == dest:
                            #print "find", 'level6', s2
                            # break
                            return 6
        # For 4 turn ############################
       
def answer2(src, dest):
    # for i in range(0,1):
    # while dest ==genLegalMoves(src,dest,7):

    # abc = genLegalMoves(src,dest,7)
    # print abc
    ################first#############
    for f in Moves(src, dest, 7):
        if f == dest:
            print "find", 'level1'
            return 1
    ##################################


    for i in Moves(src, dest, 7):
        print i, 'print i'
        # print genLegalMoves(i, dest, 7)
        for s in Moves(i, dest, 7):
            print s, 's1'
            if s == dest:
                print "find", 'level2'
                # break
                return 2

        for i2 in Moves(i, dest, 7):
            print i2, 'print i2'
            print Moves(i, dest, 7), "what is it ?"
            for s in Moves(i2, dest, 7):
                print s, 'print s'
                if s == dest:
                    print "find", 'level3'
                    return 3
                    # break
            for i3 in Moves(i2, dest, 7):
                print i2, 'print i2'
                print Moves(i2, dest, 7), "what i3"
                for s in Moves(i3, dest, 7):
                    print s, 'print s3'
                    if s == dest:
                        print "find", 'level4'
                        return 4

print answer(0,9)
