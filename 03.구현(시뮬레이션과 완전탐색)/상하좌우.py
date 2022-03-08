#입력받기
# n = int(input())
# order=input().split()
# n =int("5")
# order=("R R R U D D").split()
#
# #현재위치
# x,y =1,1
#
# #LRUD
# # dx=[0,0,-1,1]
# # dy=[-1,1,0,0]
# #RULD 이동방향
# dx=[0,-1,0,1]
# dy=[1,0,-1,0]
#
# for o in order:
#     if x >1 :
#         if o=='U' :
#             x+=dx[1]
#             y+=dy[1]
#     if x < n :
#         if o=='D' :
#             x+=dx[3]
#             y+=dy[3]
#     if y >1 :
#         if o=='L' :
#             x+=dx[2]
#             y+=dy[2]
#     if y < n :
#         if o=='R' :
#             x+=dx[0]
#             y+=dy[0]
#
# print(x,y)


# 해답=============================
#입력받기
# n = int(input())
# order=input().split()
n =int("5")
order=("R R R U D D").split()

#현재위치
x,y =1,1

#RULD 이동방향
dx=[0,-1,0,1]
dy=[1,0,-1,0]

moves =['R', 'U', 'L', 'D']

for o in order:
    for i in range(len(moves)):
        if o == moves[i]:
            nx = x+dx[i]
            ny = y+dy[i]
            print('nx.ny:%d, %d'%(nx,ny) )
    if nx<1 or ny <1 or nx >n or ny >n:
        continue
    #이동수행
    x, y=nx,ny

print(x,y)
