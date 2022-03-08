print((lambda x,y : x+y)(3,7))
print('=======')
#여러개의 리스트 더하기
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = [6,7,8,9,10]
res1=list(map((lambda x,y,z: x+y+z),list1,list2,list3))
print(res1)
