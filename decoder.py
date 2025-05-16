import string
alphabet = []
for i in string.ascii_lowercase:
    alphabet.append(i)
alphabet.append(' ')
def decode(string):
    strList = []
    for i in range(26):
        continueStep = True
        decodeStr = ''
        for j in string:
            shifted = chr(((ord(j) + (i)) % 26) + 97)
            if not (shifted in alphabet):
                continueStep = False
                break
            elif j != ' ':
                decodeStr += shifted
            else:
                decodeStr += ' '
        if continueStep:
            strList.append(decodeStr + '\n')
    return strList