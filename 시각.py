from itertools import permutations
# sel = int(input())
sel = int("5")

# hour = #sel~23
# minuite = #0~59
# second = #0~59
count=0
for i in range(sel+1):
    for m in range(60):
        for s in range(60):
            #매 시각안에 문자'3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(m) + str(s): #문자열 나열
                count+=1
print(count)
