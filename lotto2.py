import random

# Create lotto List
lotto=[]

# 1 ~ 45 number insert
for number in range(1,46):
    lotto.append(number)

print(lotto)

# choice 6 numbers
# lotto list 에서 뽑아 낼수 있다면

#choice=random.randint(lotto)
sel_lotto=[]
for num in range(6):
    sel_num=random.choice(lotto)
    print(sel_num)
    sel_lotto.append(sel_num)
    lotto.remove(sel_num)   # 값을 지워 버림
    print(lotto)

print("Lotto Number: ", sel_lotto)
print("Service Number : ", random.choice(lotto))

