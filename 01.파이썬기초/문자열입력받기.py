# =======input으로 받기 ========
#방법1) 1개의 변수에 리스트로 받기
# data = list(map(int,input().split()))
# print(data)
# #방법2) 각각의 변수에 값 담기
# a,b,c,=map(int,input().split())
# print(a,b,c)

# =======빠르게 입력받기 (readline()) ========
import sys
#문자열 입력받기
# data1=sys.stdin.readline().rstrip() #rstrip(): 마지막에 들어오는 엔터기호빼기
# print(data1)


#f-string예제
answer =7
print(f'정답은 {answer} 입니다.')
