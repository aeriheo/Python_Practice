def solution(answers):
    answer = []
    stu_1 = [1, 2, 3, 4, 5]
    stu_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    stu1 = 0
    stu2 = 0
    stu3 = 0
    for i in range(len(answers)):
        if answers[i] == stu_1[i%len(stu_1)]:
            stu1+=1
        if answers[i] == stu_2[i%len(stu_2)]:
            stu2+=1
        if answers[i] == stu_3[i%len(stu_3)]:
            stu3+=1
    max = 0
    if max<stu1:
        max = stu1
    if max<=stu2:
        max = stu2
    if max<=stu3:
        max = stu3

    if max==stu1:
        answer.append(1)
    if max==stu2:
        answer.append(2)
    if max==stu3:
        answer.append(3)
    print(answer)
    return answer

answers = [1,2,3,4,5]
solution(answers)