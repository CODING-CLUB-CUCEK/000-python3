def average(array):
    # your code goes here
    array = set(array)
    result = sum(array)/len(array)
    result = round(result,3)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)