# List Manipulation

def addName(nameListAux):
    """Returns a list of names

    Args:
        aux str: name that will add to the list list
    """

    name = str(input('Enter a new name: '))

    while name != 'quit':

        nameListAux.append(name)
        print(nameListAux)
        name = str(input('Enter a new name: '))1

    print(nameListAux)
    return nameListAux


def searchName(searchedNameList):
    name = str(input('Enter name to be searched: '))

    listLength = int(len(searchedNameList))

    while (listLength //  2) >= int(len(searchedNameList)):
        if name == searchedNameList[listLength]:
            return print('the name is at position', listLength)
        listLength += 1
    
    listLength = int(len(searchedNameList))

    while (listLength // 2) <= 0:
        if name == searchedNameList:


if __name__ == '__main__':
    nameList = []
    while True:
        switch = int(input('''Choose a option:
        1- Add name to list
        2- Search for name in list
        '''))
        if switch == 1:
            addName(nameList)
            print(nameList)
        if switch ==2
