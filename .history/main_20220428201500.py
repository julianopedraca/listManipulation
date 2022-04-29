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

    listLength = (int(len(searchedNameList)) // 2) -1
    print(listLength)
    print(listLength // 2)

    while ((listLength // 2) - 1) <= (int(len(searchedNameList) - 1)):
        if name == searchedNameList[listLength]:
            return print('the name is at position', listLength)
        listLength += 1
        print(listLength)

    listLength = int(len(searchedNameList))

    while ((listLength // 2) - 1) >= 0:
        if name == searchedNameList[listLength]:
            return print('the name is at position', listLength)
        listLength -= 1
        print(listLength)


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
            print(nameList)
            print(nameList[2])
        if switch == 2:
            searchName(nameList)
