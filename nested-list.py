if __name__ == '__main__':
    students = []
    scores = []

    # taking inputs of all students and populating them in student and scores arr 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name,score])

    # chage the array into set and sort them 
    sorted_scores = sorted(set(scores))
    
    result = []
    
    # iterate through the element and find the students that has the second lowest score
    for student in students:
        if student[1] == sorted_scores[1]:
            result.append(student[0])
    
    # print the result name in sorted order
    for x in sorted(result):
        print(x)            
        
