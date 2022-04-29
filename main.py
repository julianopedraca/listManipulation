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
        name = str(input('Enter a new name: '))

    print(nameListAux)
    return nameListAux


def searchName(searchedNameList):
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


if __name__ == '__main__':
    # nameList = [] -- alterar apos o código ficar pronto
    nameList = ['joao', 'maria', 'carla', 'joaquina', 'pedro', 'seis', 'sete']
    while True:
        switch = int(input('''Choose a option:
        1- Add name to list
        2- Search for name in list
        '''))
        if switch == 1:
            addName(nameList)

        if switch == 2:
            searchName(nameList)
