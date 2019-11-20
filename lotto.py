import random

# Create lotto List
lotto=[]

# 1 ~ 45 number insert
for number in range(1,46):
    lotto.append(number)

print(lotto)

# choice 6 numbers
# for 문 보다는 while 문을....len(lotto2) = 6일 때 까지..
# Service number 때문에 7번 실
lotto2=[]
print(len(lotto2))
#for num in range(6):   # number
for num in range(7):   # service number 
    choice=random.randint(1,45)
    print(choice)
    print("first : " ,lotto2)
    # 중복 제거 
    if choice in lotto2:
        print(choice)
        print("double")
        # 재수 없게 중복 되면?
        choice=random.randint(1,45)
    lotto2.append(choice)    
    print(lotto2)
    print("==========================")
