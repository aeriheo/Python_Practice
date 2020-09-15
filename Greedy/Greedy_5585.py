# 입력값
data = int(input())

# 남은돈
money = 1000 - data

# 500엔의 개수
yen_500 = int(money / 500)

# 남은 돈
left = money%500
# 100엔의 개수
yen_100 = int(left/100)
left = left%100

# 50엔의 개수
yen_50 = int(left/50)
left = left%50

# 10엔의 개수
yen_10 = int(left/10)
left = left%10

# 5엔의 개수
yen_5 = int(left/5)
# 1엔의 개수
yen_1 = left%5

result = yen_500 + yen_100 + yen_50 + yen_10 + yen_5 + yen_1
print(result)