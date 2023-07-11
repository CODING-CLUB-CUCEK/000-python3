if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        '''
        In this section, a loop is used to iterate n times and read the names and marks of the students.
        Inside the loop, input().split() is used to read a line of input and split it into a list of values. 
        The first value is stored in the variable name, and the remaining values are stored in the list line.
        '''
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]
    average = sum(marks)/len(marks)
    print("{:.2f}".format(average))
