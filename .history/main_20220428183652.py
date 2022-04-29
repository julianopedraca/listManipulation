# List Manipulation

def addName(nameFunc):
    """Returns a list of names

    Args:
        aux str: name that will add to the list list
    """

    name = str(input('Enter a new name: '))

    while name != 'quit':

        nameFunc.append(aux)
        print(nameFunc)
        aux = str(input('Enter a new name: '))

    print(nameFunc)
    return nameFunc

if __name__ == '__main__':
    nameList = []
    while True:
        switch = int(input('''Choose a option:
        1- Add name to list
        '''))
        if switch == 1:
            nameList.append(addName(nameList))
            print(nameList)
