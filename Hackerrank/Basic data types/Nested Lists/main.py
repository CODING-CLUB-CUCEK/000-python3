if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest score
    scores = [student[1] for student in students]
    second_lowest_score = sorted(set(scores))[1]

    # Find students with the second lowest score
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]

    # Sort the names alphabetically
    second_lowest_students.sort()

    # Print the names of students with the second lowest score
    for student in second_lowest_students:
        print(student)
