

'''
Playfair Cipher Assignment

@author: Kevin Griffith
'''

table = None
finalKeyString = None

def findIndex(table, item):
    """finds item in the cipher table, and returns its index as the first and second element in a list"""
    # return [(ind,table[ind].index(item)) for ind in range(len(table)) if item in table[ind]]
    output = []
    for i, e in enumerate(table):
        for j,ee in enumerate(e):
            if item in ee:
                #print(i,j)
                output.append(i)
                output.append(j)
                # print(output)
                return output


def set_key(key):
    """Set the key to be used by the cipher."""
    global finalKeyString
    key = key.upper().replace(" ","")
    keyListNoDupes = list(dict.fromkeys(key))
    finalKeyString = ''.join(keyListNoDupes)
    #print(finalKeyString)
    return finalKeyString


def get_table(key):
    """Returns a list of lists with the key table formatted as a 5x5 block"""
    global finalKeyString
    if finalKeyString is None:
        raise RuntimeError('You must run set_key(key) before you can run get_table().')
        return None
    keyphrase = set_key(key)
    print(keyphrase)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if "I" in keyphrase:
        alphabet = alphabet.replace("J", "")
    elif "J" in keyphrase:
        alphabet = alphabet.replace("I", "")
    elif "I" or "J" not in keyphrase:
        alphabet = alphabet.replace("IJ", "I")
    keyPlusAlphaBet = keyphrase + alphabet
    keyPlusAlphaBet = list(dict.fromkeys(keyPlusAlphaBet))
    #print(keyPlusAlphaBet)
    parentList = [keyPlusAlphaBet[x:x+5] for x in range(0,len(keyPlusAlphaBet),5)]
    for x in parentList:
        print(*x)
    return parentList


def encrypt(plaintext):
    """Encrypt using the Playfair cipher and return the encrypted plaintext"""
    global table, finalKeyString
    if table is None:
        table = get_table(finalKeyString)
    output = []
    plaintext = plaintext.upper().replace(" ","")
    inputText = list(plaintext)
    #print(inputText)
    for x in range(len(inputText)-1):
        if inputText[x] == inputText[x+1]:
            inputText.insert(x+1,'X')
    if (len(inputText) % 2 != 0):
        inputText.append("X")
    inputText = [inputText[x:x+2] for x in range(0,len(inputText),2)]
    #print(inputText)
    for x in inputText:
        first = []
        second = []
        for y in x:
            if y == x[0]:
                first = findIndex(table, y)
                # print(first)
            elif y ==x[1]:
                second = findIndex(table, y)
                #print(second)

        if first[0] != second[0] and first[1] != second[1]: #opposite corners
            output.append(table[first[0]][second[1]])
            output.append(table[second[0]][first[1]])

        elif first[0] != second[0] and first[1] == second[1]: #different rows, same column
            if first[0] == 4 and second[0] != 4: #case if letter is in last row
                output.append(table[0][first[1]])
                output.append(table[second[0] + 1][first[1]])
            elif second[0] ==4 and first[0] != 4: #case if letter is in last row
                output.append(table[first[0] + 1][first[1]])
                output.append(table[0][first[1]])
            else:
                output.append(table[first[0]+1][first[1]]) #case if letter no on last row
                output.append(table[second[0] + 1][first[1]])

        elif first[0] == second[0] and first[1] != second[1]: #same row, different colum
            if first[1] == 4 and second[1] != 4:
                output.append(table[first[0]][0])
                output.append(table[second[0]][second[1] + 1])
            elif second[1] == 4 and first[1] != 4:
                output.append(table[first[0]][first[1] + 1])
                output.append(table[first[0]][0])
            else:
                output.append(table[first[0]][first[1]+1])
                output.append(table[second[0]][second[1]+1])

    print(''.join(output))
    return output








def decrypt(ciphertext):
    """Decrypt using the Playfair cipher and return the plaintext."""
    output = []
    ciphertext = [ciphertext[x:x+2] for x in range(0,len(ciphertext),2)]
    #print(ciphertext)

    for x in ciphertext:
        first = []
        second = []
        for y in x:
            if y == x[0]:
                first = findIndex(table, y)
                # print(first)
            elif y ==x[1]:
                second = findIndex(table, y)
                #print(second)

        if first[0] != second[0] and first[1] != second[1]: #opposite corners
            output.append(table[first[0]][second[1]])
            output.append(table[second[0]][first[1]])

        elif first[0] != second[0] and first[1] == second[1]: #different rows, same column
            if first[0] == 0 and second[0] != 0: #case if letter is in last row
                output.append(table[4][first[1]])
                output.append(table[second[0] - 1][first[1]])
            elif second[0] ==0 and first[0] != 0: #case if letter is in last row
                output.append(table[first[0] - 1][first[1]])
                output.append(table[4][first[1]])
            else:
                output.append(table[first[0]-1][first[1]]) #case if letter no on last row
                output.append(table[second[0] - 1][first[1]])

        elif first[0] == second[0] and first[1] != second[1]: #same row, different colum
            if first[1] == 0 and second[1] != 0:
                output.append(table[first[0]][4])
                output.append(table[second[0]][second[1] + 1])
            elif second[1] == 0 and first[1] != 0:
                output.append(table[first[0]][first[1] + 1])
                output.append(table[first[0]][4])
            else:
                output.append(table[first[0]][first[1]-1])
                output.append(table[second[0]][second[1]-1])
    print(''.join(output))
    
    return ''.join(output)



if __name__ == '__main__':
    import sys

    print("Enter desired keyphrase:")
    keyphrase = input()
    print("Enter the phrase you want encrypted:")
    phrase = input()
    set_key(keyphrase)
    table = get_table(keyphrase)
    encryptedPhrase = encrypt(phrase)
    decrypt(encryptedPhrase)

    sys.exit(0)

    
    
    
