from collections import Counter
def countStudents (students, sandwiches):
    dic1 = Counter(students)
    print(dic1)
    dic2 = Counter(sandwiches)
    for c in sandwiches:
        if dic1[c] != 0:
            dic1[c] -= 1
        else:
            break
    return sum(dic1.values()) 






print(countStudents( [0,0,0,1,0,1,1,1,1,0,1],[0,0,0,1,0,0,0,0,0,1,0]))