import numpy as np
s = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

resultSet=[] #최종 반환값
def solution(places):
    pList=[]
    for eaClass in places : #한 교실씩 읽기
        print('한 교실은: ',eaClass) #한 교실
        # x,y=0,0
        x1,x2=0,0
        y1,y2=0,0
        result =""
        rowCheck=1
        for eaRow_ in eaClass: #교실별 한행씩 읽기
            if rowCheck !=0 :
                eaRowElmt = list(eaRow_)
                print('eaRowElmt: ',eaRowElmt) #각 행을 리스트로 변환
                eaRowPindex=list(filter(lambda y: eaRow_[y] == 'P', range(len(eaRow_)))) #각 행에서 P 인덱스 리스트
                #한 행별 거리 확인하기 =============
                for elmt in range(len(eaRowPindex)-1): #각 줄에서 p 거리 확인
                    y1 = eaRowPindex[elmt]
                    y2 = eaRowPindex[elmt+1]
                    print('y1= %d, y2= %d' %(y1, y2))
                    # print('eaRowPindex(=y 포지션) : ',eaRowPindex)
                    if rowCheck ==0 :
                        break
                    elif y2- y1 <=2:
                        # print('y2- y1 = %d'%(y2- y1))
                        print('한 행별 거리 확인하기 =============break!!!!!') #거리유지 안됨!!
                        rowCheck=0
                        break
            x1 +=1 #다음행으로 이동
            x2 = eaRowPindex[elmt+1]
            print('x1= %d, x2= %d' %(x1, x2))
            # 아래 위 행끼리 확인 ===========
            # if
        pList=[]
    answer = places
    return answer

print(solution(s))
