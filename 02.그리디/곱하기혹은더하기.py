#각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 가장 큰수를 구하기.

#입력받기
# n=list(input())
n="567"
#첫번째 문자를 숫자로 변경하여 대입
result=int(n[0])
print(result)
print(type(result))

for i in range(1, len(n)):
    num = int(n[i])
    if num<=1 or result <=1:
        result+=num
    else:
        result*=num
print(result)
