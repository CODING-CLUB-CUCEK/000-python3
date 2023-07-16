def SymmetricDifference(N,M):

    symmetricDifference = sorted(M.union(N) - M.intersection(N))

    for values in symmetricDifference:
        print(values)

if __name__ == '__main__':
        # Enter your code here. Read input from STDIN. Print output to STDOUT
    M = int(input())
    M = set(map(int,input().split()))

    # Enter your code here. Read input from STDIN. Print output to STDOUT
    N = int(input())
    N = set(map(int,input().split()))
    SymmetricDifference(N,M)