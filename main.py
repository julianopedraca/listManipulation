"""List Manipulation"""


def addName(nameListAux):
    """Returns a list of names

    Args:
        aux str: name that will add to the list list
    """

    name = str(input('Enter a new name: '))

    while name != 'quit':

        nameListAux.append(name)
        print(nameListAux)
        name = str(input('Enter a new name: '))

    print(nameListAux)
    return nameListAux


def searchName(searchedNameList):
    """Search a name on the list

    Args:
        searchedNameList list: list that will search the name

    Returns:
        int: position of the name in the list
    """
    name = str(input('Enter name to be searched: '))

    listLength = (int(len(searchedNameList)) // 2) - 1

    while listLength <= (int(len(searchedNameList) - 1)):
        if name == searchedNameList[listLength]:
            return print('the name is at position', listLength)
        listLength += 1

    listLength = (int(len(searchedNameList)) // 2) - 1

    while listLength >= 0:
        if name == searchedNameList[listLength]:
            return print('the name is at position', listLength)
        listLength -= 1


def excludeName(nameToBeExcludedList):
    """call function remove to exclude selected name

    Args:
        nameToBeExcludedList list: list that will remove desired name
    """

    name = str(input('Wich name do you want to exclude? '))

    nameToBeExcludedList.remove(name)


if __name__ == '__main__':

    nameList = []

    selectionDict = {
        1: addName,
        2: searchName,
        3: excludeName,
        4: print,
    }

    while True:
        switch = int(input('''Choose a option:
        1- Add name to list
        2- Search for name in list
        3- Enter a name to be excluded from list
        4- Print list
        '''))
        selectionDict[switch](nameList)
