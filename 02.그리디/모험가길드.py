'''
# person *n = {"공포도" : x}
# groups ={
    group1[person * ?],
    group2[person * ?]
    ...
}
# person["공포도"] >= len(group)
#그룹의 최대값? gongpoNum???
'''

# n = list(map(int,input().split()))
# n = list(map(int,("2 3 1 2 2").split()))
# # print('origin: ',n)
# n.sort() #오름차순 정렬
# print('sort: ',n)
# group=0 #총 그룹 수
# while True:
#     if len(n)==0:
#         break
#     gongpoNum=n[0] #공포도 가장 큰 수 찾기
#     print('gongpoNum(공포도): ',gongpoNum)
#
#     #남은 모험가 수가 공포도 보다 크면,
#     if gongpoNum <=len(n):
#         #현재 공포도의 인원만큼 그룹으로 묶고
#         temp=n[:gongpoNum]
#         print('temp: ',temp)
#         print('그룹내 공포도 최고: ',max(temp))
#         if gongpoNum == max(temp) and gongpoNum<= len(temp):
#             #그룹내 공포도 최고치와 그룹인원이 동일한지 확인.
#             del n[:gongpoNum]
#             group+=1
#             print('그룹결성!!')
#             print('남은 그룹: ',n)
#         else:
#             print('뭐지??')
#             break
#     else:
#         break
#
# print('최대그룹수: ', group)

#해답 ================
# n = list(map(int,input().split()))
n = list(map(int,("2 3 1 2 2").split()))
n.sort() #오름차순 정렬

result=0 #총 그룹 수
count=0 #현재 그룹에 포함된 모험가의 수

for i in n:
    count+=1
    if count >= i:
        result +=1
        count =0
print(result)
