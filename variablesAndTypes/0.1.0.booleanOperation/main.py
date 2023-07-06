
def booleanOperations():
    print("boolean operations")
    print("There are mainly 3 boolean operations in python")
    print("\n 1. and \n 2. or \n 3. not")
    option = int(input("choose any one of them"))
    #in python we don't have switch case statement ,so we use match case statement instead of switch case statement 
    match option:
        case 1:
            booleanAnd()
        case 2:
            booleanOr()
        case 3:
            booleanNot()
        case _:
            print("invalid option")


def booleanAnd():
    varA = 1 
    varB = 0
    print("varA = 1")
    print("varB = 0")
    print("varA and varB = ",varA and varB)

def booleanOr():
    varA = 1 
    varB = 0
    print("varA = 1")
    print("varB = 0")
    print("varA or varB = ",varA or varB)

def booleanNot():
    varA = 1 
    varB = 0
    print("varA = 1")
    print("varB = 0")
    print("not varA = ",not varA)
    print("not varB = ",not varB)


def main():
    #call boolean operations 
    booleanOperations()


if __name__ == '__main__':
    main()    