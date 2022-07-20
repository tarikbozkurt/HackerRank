if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = 0
    dived_x = 0
    for k in student_marks:
        if k == query_name:
            values = student_marks[k]
            for i in values:
                result +=i
                dived_x +=1
    
    print('{0:.2f}'.format(result/dived_x))
                
