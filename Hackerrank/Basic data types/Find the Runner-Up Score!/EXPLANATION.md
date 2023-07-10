## Explanation:

The variable ``` n```  is used to store the number of scores. It is obtained from the user input.
The ```arr```  list is created by using ```map``` and ```list()```  functions.```  map(int, input().split())```  converts the input string of scores into a list of integers.
To find the runner-up score, we need to remove duplicates and sort the scores in descending order.
```set(arr)``` converts the list arr into a set to remove duplicate scores.
```sorted(arr, reverse=True)```  sorts the unique scores in descending order using the sorted() function.
The runner-up score is the second highest score in the sorted list. We access it using arr[1].
Finally, we print the runner-up score using ```print(arr)``` 