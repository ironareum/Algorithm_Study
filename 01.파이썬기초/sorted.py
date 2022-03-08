#sorted(정렬할데이터, key파라미터, reverse파라미터)
'''
-key옵션:정렬의 기준이 되는 키값 정해주기
-reverse옵션 : 디폴트=False=오름차순

*리스트.sort() vs sorted()
-리스트.sort(): 본체의 리스트를 정렬해서 변환
-sorted(): 본체 리스트는 그대로 두고, 정렬한 새로운 리스트를 반환
'''

import operator

# 딕셔너리
d = dict()
d['a'] = 66
d['i'] = 20
d['e'] = 30
d['d'] = 33
d['f'] = 50
d['g'] = 60
d['c'] = 22
d['h'] = 80
d['b'] = 11


# print("============")
# 1. 딕셔너리 출력
print("\n1. 기본 딕셔너리")
print(d)

print(sorted(d)) #key값만 정렬해서 보여줌
print(sorted(d.items())) #key 기준으로 아이템들 정렬해서 보여줌
print(sorted(d.items(), reverse=True)) #key값 내림차순 정렬

#딕셔너리 value 정렬
print('#방법1) (operator 모듈 이용)')
#방법1) (operator 모듈 이용)
print(sorted(d.items(), key=operator.itemgetter(1)))
print(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

print('#방법2) 람다 이용')
#방법2) 람다 이용
print(sorted(d.items(), key=(lambda x:x[1])))
print(sorted(d.items(), key=(lambda x:x[1]), reverse=True))
