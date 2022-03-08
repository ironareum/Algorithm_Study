# n = inpu()
n = "514"
# print(n)
count=0
l=len(n)
list=[]
if l ==1: #1자리
    if n%2!=0:
        count+=1
    break #종료
if l == 2: #2자리
    for i in n:
        if i%2!=0:
            count+=1
        n=0
        n+=i
        print()
else : #3자리 이상
    devide=l//3 #몇개씩 나눌지
    left=l%3
    print('devide: %d, left: %d' %(devide, left))
    n()

## 풀다맘...
