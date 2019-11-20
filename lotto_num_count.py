import random
import copy
import pprint

# lotto insert times LC
# searching number and count
LC = 20

# Create lotto List
Lotto_Ball=[]
Lotto_Num=[]

# Create Lotto Dictionary
LottoDic={}   # LottoDic=dict()

# Lotto_Ball 담기
# 1 ~ 45 number insert
for number in range(1,46):
    Lotto_Ball.append(number)

print("===== Ball Insert")    
print(Lotto_Ball)

for count in range(LC):
# 공 copy
    Lotto_Ball2 = copy.deepcopy(Lotto_Ball)

    print("===== Ball2 Insert")    
    print(Lotto_Ball2)
    
# Lotto 뽑기
    # 초기화
    Lotto_Num=[]
    Lotto_Svr=[]
    
    for num in range(6):
        Sel_Num=random.choice(Lotto_Ball2)
        print(Sel_Num)
        Lotto_Num.append(Sel_Num)
        Lotto_Ball2.remove(Sel_Num)   # 값을 지워 버림
        print(Lotto_Num)

    print("Lotto Number: ", Lotto_Num)
    Lotto_Srv=random.choice(Lotto_Ball2)
    print("Service Number : ", Lotto_Srv)

# Lotto 번호 저장 하기
# {1:{'L_N': [1,2,3,4,5,6],
#     'L_S': [7]}}

    LottoDic.setdefault(count+1,{'L_N':Lotto_Num,
                               'L_S':Lotto_Srv})

############ 여기 까지 10회 입력
# 내용 확인
#pprint.pprint(LottoDic)
LottoNumCount={}

for k,v in LottoDic.items():
    #print(k,v)
    print(LottoDic[k]['L_N'])  # 숫자만 가져 오기 가능
    
    for lottonum in LottoDic[k]['L_N']:
        if lottonum in LottoNumCount:
            LottoNumCount[lottonum] += 1            
        else:
            LottoNumCount.setdefault(lottonum,1)
            
    #print(LottoNumCount)
            
def f2(x):
    #print(x)
    #print(type(x))
    #print(x[1])
    return x[1]

res = sorted(LottoNumCount.items(), key=f2, reverse = True)
print(res)
#print(type(res))  # List

for num1 in range(6):  # 상위 숫자 6개만 뽑기, 횟수가 같은 6번째숫자는 어떻게? 동률
    print(res[num1])
    print("숫자 :", res[num1][0],  "횟수 : ",  res[num1][1])
    #print(res[num1][1])
    #print('숫자 :[{0:3d}], 횟수 :[{1:>3d}]'.format(res[num1][0], res[num1][1]))
    #print('숫자 :[{0:3d}], 횟수 :[{0:>3d}]'.format(res[num1][0], res[num1][1]))
    print('숫자 :[{}], 횟수 :[{}]' .format(res[num1][0], res[num1][1]))
    # print(type(res[num1]))  # tuple

        


# 추후 DB 연동(lotto numbers)

