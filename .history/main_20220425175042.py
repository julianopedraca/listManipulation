# List Manipulation

def addName(aux):
    """Add 

    Args:
        aux (_type_): _description_
    """
    nameList = []
    aux = str(input('Enter a new name: '))

    while aux != 'quit':

        nameList.append(aux)
        print(nameList)
        aux = str(input('Enter a new name: '))

    print(nameList)
