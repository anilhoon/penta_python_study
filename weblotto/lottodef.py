import random
import copy
import pprint


Lotto_Ball=[]
Lotto_Num2=[]
Lotto_Svr=[]
LottoDic={} 

def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

def load_box_ball(ball_num: int='45') -> list:
    
    Lotto_Box=[]
    # Lotto_Ball 담기
    # 1 ~ 45 number insert
    for number in range(1,int(ball_num) + 1):
        Lotto_Box.append(number)
    return list(Lotto_Box)

def sel_box_ball(Lotto_Box:list, ronum: int='1') -> set:
    LottoDic = {}
    for count in range(int(ronum)):
        Lotto_Box2 = copy.copy(Lotto_Box)
        Lotto_Num=[]
        # Lotto 뽑기
        for num in range(6):
            #random 함수는 set 이 아니고 list
            Sel_Ball=random.choice(Lotto_Box2)
            #print(Sel_Ball)
            Lotto_Num.append(Sel_Ball)
            Lotto_Box2.remove(Sel_Ball)   # 값을 지워 버림
            #print(Lotto_Num)
        
        # Service 번호
        Lotto_Srv=random.choice(Lotto_Box2)

        # Lotto 번호 저장 하기
        # {1:{'L_N': [1,2,3,4,5,6],
        #     'L_S': [7]}}
        LottoDic.setdefault(count+1,{'L_N':Lotto_Num,
                                     'L_S':Lotto_Srv})
    return dict(LottoDic)

def lotto_sort(LottoDic: dict) -> set:
    LottoNumCount={}
    SortLottoNumCount={}

    for k,v in LottoDic.items():
        #print(k,v)
        #print(LottoDic[k]['L_N'])  # 숫자만 가져 오기 가능
    
        for lottonum in LottoDic[k]['L_N']:
            if lottonum in LottoNumCount:
                LottoNumCount[lottonum] += 1
            else:
                LottoNumCount.setdefault(lottonum,1)
                
        def f2(x):
            #print(x)
            #print(type(x))
            #print(x[1])
            return x[1]

    SortLottoNumCount = sorted(LottoNumCount.items(), key=f2, reverse = True)
    print(SortLottoNumCount)
    return dict(SortLottoNumCount)    

def lotto_num_seq(SortLottoNumCount: dict, level_num: int='6') -> set:
    LevelLottoNum={}
    for key, value in SortLottoNumCount.items():
        #print(key, value)
        if value in LevelLottoNum:
            LevelLottoNum[value] = str(LevelLottoNum[value]) + ',' + str(key)
            #print(LevelLottoNum[value])
        else:
            LevelLottoNum.setdefault(value,key)

    return dict(LevelLottoNum)


