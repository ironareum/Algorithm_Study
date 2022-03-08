# first=int("472")
# second="385"
first=int(input())
second=input()
hap=0
ea=[]
l=len(second)
j=1
# print(first, type(first))
# print(l, type(len))
for i in range(l-1,-1,-1):
    result=first* int(second[i])
    print(result)
    ea.append(result)
    hap+=result*j
    j*=10
print(hap)
