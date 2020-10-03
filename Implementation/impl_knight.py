data = input()
x = int(data[1])
# a = 97 , h = 104
y = ord(data[0])
cnt = 0
if y>=98 :
    if x>=3 and x<=6:
        cnt +=2
    elif x>=3 or x<=6:
        cnt += 1
if y>=99:
    if x>=2 and x<=7:
        cnt +=2
    elif x>=2 or x<=7:
        cnt += 1
if y<=103:
    if x>=2 and x<=7:
        cnt +=2
    elif x>=2 or x<=7:
        cnt += 1
if y<=102:
    if x>=3 and x<=6:
        cnt +=2
    elif x>=3 or x<=6:
        cnt += 1
print(cnt)