#!/usr/bin/env python3
"""Find words in a rectangular jumble


"""
pz = ['veqas'
    ,'mrlxt'
    ,'hello'
    ,'thiei'
    ,'gtwoc']

sh = []

wl = []


def showlist(lst):
    """Print out each line in an array

    Args:
        lst - a list type variable

    Returns:
        A text representation of the entire word jumble puzzle
    """
    for line in lst:
        print(' '.join(list(line)))


def loadwordlist(path):
    try:
        wlfile = open(path)
        while wl:
            wl.pop()
        for line in wlfile:
            wl.append(line.rstrip())
        print('Word list loaded successfully.  Run "findall()" to see all solutions.')
    except:
        print('Could not load word list from path')
    finally:
        wlfile.close()


def loadpuzzle(path):
    try:
        pzfile = open(path)
        while pz:
            pz.pop()
        for line in pzfile:
            pz.append(line.rstrip())
        showlist(pz)
    except:
        print('Could not load puzzle from path')
    finally:
        pzfile.close()


def showpuzzle():
    showlist(pz)


def showsearchhelper():
    if len(sh) == 0:
        buildsearchhelper()
    showlist(sh)

def buildsearchhelper():
    linetext = ''
    linepos = []
    pzwidth = len(pz[0])
    pzheight = len(pz)

    # set up horizontal lines
    for linenum in range(pzheight):
        linetext = pz[linenum]
        linepos = []
        for i in range(len(pz[linenum])):
            linepos.append((linenum, i))
        sh.append((linetext.upper(), linepos))

    # set up for vertical lines
    for colnum in range(pzwidth):
        linetext = pz[0][colnum]
        linepos = [(0, colnum)]
        for linenum in range(1, pzheight):
            linetext += pz[linenum][colnum]
            linepos.append((linenum, colnum))
        sh.append((linetext.upper(), linepos))

    # set up for \ diagonal lines
    for c in range(pzwidth):
        linetext = pz[0][c]
        linepos = [(0, c)]
        cd = c
        for r in range(1, pzheight):
            cd += 1
            if cd < pzwidth:
                linetext += pz[r][cd]
                linepos.append((r, cd))
        sh.append((linetext.upper(), linepos))
    for r in range(1, pzheight):
        linetext = pz[r][0]
        linepos = [(r, 0)]
        rd = r
        for c in range(1, pzwidth):
            rd += 1
            if rd < pzheight:
                linetext += pz[rd][c]
                linepos.append((rd, c))
        sh.append((linetext.upper(), linepos))

    # set up for / diagonal lines
    for c in range(pzwidth):
        linetext = pz[0][c]
        linepos = [(0, c)]
        cd = c
        for r in range(1, pzheight):
            cd -= 1
            if cd >= 0:
                linetext += pz[r][cd]
                linepos.append((r, cd))
        sh.append((linetext, linepos))
    for r in range(1, pzheight):
        linetext = pz[r][pzwidth - 1]
        linepos = [(r, pzwidth - 1)]
        rd = r
        for c in range(pzwidth - 2, -1, -1):
            rd += 1
            if rd < pzheight:
                linetext += pz[rd][c]
                linepos.append((rd, c))
        sh.append((linetext, linepos))
    # add reversals of all current lines
    shlen = len(sh)
    for i in range(shlen):
        linetext = sh[i][0][::-1]
        linepos = sh[i][1][::-1]
        if len(linetext) > 1:
            sh.append((linetext, linepos))


def findword(word):
    """Print out the found word in the puzzle.

    Args:
        none

    Returns:
        A text representation of the entire word jumble puzzle
        Only the letters of the found word will display.
        All other letters in the puzzle will display as an asterix.

    Test words:
            tilt
            let
            ill
            at
            axle
            there
            hello
            cow
    """
    word = word.replace(' ', '').upper()
    # build search helper only on the first find operation
    if len(sh) == 0:
        buildsearchhelper()

    sf = []
    found = []
    foundstart = -1

    for linetext, linepos in sh:
        foundstart = linetext.find(word)
        if foundstart > -1:
            for pos in linepos[foundstart: foundstart + len(word)]:
                found.append(pos)
            #break

    for linenum in range(len(pz)):
        newline = '*' * len(pz[linenum])
        for row, col in found:
            if row == linenum:
                newline = newline[:col] + pz[row][col].upper() + newline[col + 1:]
        sf.append(newline)

    showlist(sf)


def fw(word):
    findword(word)


def findall():
    for line in wl:
        print(line + '\n')
        findword(line)
        if input('Press any key to continue or "Q" to quit.') == 'q':
            break


def testit():
    loadpuzzle('Comics_Puzzle.txt')
    loadwordlist('Comics_WordList.txt')
    findall()


if __name__ == '__main__':
    testit()
else:
    print(__name__)