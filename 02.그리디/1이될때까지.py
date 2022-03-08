# import psutil
# import os

# 어떠한 수 N이 될때까지 다음의 두 방법중 하나를 반복적으로 선택. 단 두번째 연산은 N이 K로 나누어 떨어질때만 선택가능.
#1) N에서 1빼기  2)N을 K로 나누기

n=25
k=3
# n,k=map(int,input().split())
'''
#입력받기 연습!!!!
n,k=map(int,input().split())
'''
# count=0 #수행횟수
# while True:
#     if n==1:
#         break #수행종료
#     if (n%k==0):
#         n//=k
#         count+=1
#         if n==1:
#             break
#     else:
#         n-=1
#         count+=1
# print(count)


#해답 =============
result=0
while True:
    target=(n//k)*k #k로 나누어 떨어지는 횟수 만큼의 수
    print('target: ', target)
    result+= (n-target) #나누어떨어지는수를 제외한 나머지 값
    print('result: ', result)
    n=target
    print('n: ', n)

    if n<k:
        break
    result += 1
    print('result: ', result)
    n//=k
    print('n', n)
    print('**** 한바퀴돔 ****')
result+= (n-1)
print(result)


#메모리 사용량 확인
# pid=os.getpid()
# p=psutil.Process(pid)
# print(p.memory_info())
