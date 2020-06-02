def solution(data):
    s1 = data[0] + data[1]
    s2 = data[0] - data[1]
    s3 = data[0] * data[1]
    s4 = int(data[0] / data[1])
    s5 = data[0] % data[1]
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)

data = list(map(int, input().split()))

solution(data)