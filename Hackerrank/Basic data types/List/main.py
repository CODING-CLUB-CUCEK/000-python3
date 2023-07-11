if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        cmd , *e = input().split()
        """ 
        this split the input and store the first value
        in the cmd which is generally the command and 
        the second and upcoming values in e which is 
        going to be the element of the list 
        this code works perfectly fine with the latest version of python 
        but not with the old versions .so you might get error in hackerrank use if elif instead of match everything will be alright 
        
        """ 
        match cmd:
            case "insert":
                l.insert(int(e[0]),int(e[1])) 
            case "print":
                print(l)
            case "remove":
                l.remove(int(e[0]))
            case "append":
                l.append(int(e[0]))
            case "sort":
                l.sort()
            case "pop":
                l.pop()
            case "reverse":
                l.reverse()

            