

def addName(aux):
    """_summary_

    Args:
    """_summary_
    """        aux (_type_): _description_
    """    
    nameList = []
    aux = str(input('Enter a new name: '))

    while aux != 'quit':

        nameList.append(aux)
        print(nameList)
        aux = str(input('Enter a new name: '))

    print(nameList)
