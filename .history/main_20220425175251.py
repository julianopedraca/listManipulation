# List Manipulation

def addName(aux):
    """Add name to list

    Args:
        aux str: name that will add to a list
    """
    
    nameList = []
    aux = str(input('Enter a new name: '))

    while aux != 'quit':

        nameList.append(aux)
        print(nameList)
        aux = str(input('Enter a new name: '))

    print(nameList)
