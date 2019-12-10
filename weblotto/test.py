import lottodef
import random

#rotation Num
ronum = 20
#Choice Level Num
clnum = 6

# rotation 횟수 만큼 돌리
for rot in range(ronum):
    # 공 담기
    Lotto_Ball = lottodef.GetBall()
    print(type(Lotto_Ball))
    Sel_Num=random.choice(Lotto_Ball)
    print(Sel_Num)
    aaa = str(lottodef.SelBall(Lotto_Ball))
    print(Lotto_Ball)
    ##print(aaa)

