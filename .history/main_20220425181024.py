# List Manipulation

def addName(aux):
    """Returns a list of names

    Args:
        aux str: name that will add to the list list
    """

    nameList = []
    aux = str(input('Enter a new name: '))

    while aux != 'quit':

        nameList.append(aux)
        print(nameList)
        aux = str(input('Enter a new name: '))

    print(nameList)
    return nameList

if __name__ == '__main__':
    nList = []
    while True:
        switch = str(input('Choose a option: n\
        1- Add name to list'))
        if switch == 1:
            addName(nList)
            print(nList)
