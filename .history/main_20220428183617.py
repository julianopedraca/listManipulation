# List Manipulation

def addName(naist):
    """Returns a list of names

    Args:
        aux str: name that will add to the list list
    """

    nameList = []
    name = str(input('Enter a new name: '))

    while name != 'quit':

        nameList.append(aux)
        print(nameList)
        aux = str(input('Enter a new name: '))

    print(nameList)
    return nameList

if __name__ == '__main__':
    nameList = []
    while True:
        switch = int(input('''Choose a option:
        1- Add name to list
        '''))
        if switch == 1:
            nameList.append(addName(nameList))
            print(nameList)
