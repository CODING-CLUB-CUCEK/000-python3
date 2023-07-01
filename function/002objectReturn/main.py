# main.py 
#creating class ,name of class defaultValue 
class defaultValue:

    def __init__(self, a):
        self.a = a

# creating class ,name of class lenTest
class lenTest:

    def __init__(self, a):
        self.a = a

    def __len__(self):
        # return 1 for true
        return 0


#creating class ,name of class boolTest
class boolTest():
    
    def __init__(self, a):
        self.a = a

    def __bool__(self):
    
        return False



# creating function ,name of function truthValueTest
def truthValueTest():
    """
    This function check the truth value of object in python , with and without 
    bool() function ,
    len() function
    """

    defaultValueObject = defaultValue(0)
    boolTestObject = boolTest(0)
    lenTestObject = lenTest(0)
    # by default object is true 
    print(bool(defaultValueObject))
    # by using bool() function we can set the truth value to false 
    print(bool(boolTestObject))
    # by using len() function we can set the truth value to false
    print(bool(lenTestObject))

    if defaultValueObject:
        print("defaultValueObject is true")

    if boolTestObject:
        print("boolTestObject is true")
    elif lenTestObject:
        print("lenTestObject is true")
    else:
        print("boolTestObject & lenTestObject are false")





def main():
    truthValueTest()



if __name__ == "__main__":
    main()

