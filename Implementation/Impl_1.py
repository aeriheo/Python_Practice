cnt = int(input())
data = input().split(" ")
x = 1
y = 1
for i in range(len(data)):
    if data[i] == "R" and y<cnt:
        y += 1
    elif data[i] == "L" and y>1:
        y -= 1
    elif data[i] == "U" and x>1:
        x -= 1
    elif data[i] == "D" and x<cnt:
        x += 1

print(x, y)
