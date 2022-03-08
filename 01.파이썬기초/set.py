data=set([1,1,2,3,3,3,4])
data=set({1,2,3,4,7,7,7})
data
data=set("hello")
print(data)

data.add(5)
print(data)

data.update([7,8,9])
print(data)

data.remove("h")
print(data)

subt = set("hello")
res1=data - subt

print(res1)
subt1 = set({1,2,3,4,5,6,7,8,9})
res2=data - subt1
print(res2)
