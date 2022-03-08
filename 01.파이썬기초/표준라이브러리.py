'''
#기본함수
'''
#sum, min, max
#eval(계산식)
#sorted : key, reverse

'''
#순열, 조합 : itertools 라이브러리 사용!!

# 순열: 서로다른 n개에서 서로다른 r개를 선택하여 일렬로 나열하는것.
# 예){'A','B','C'}에서 세개를 선택하여 나열하는 경우:
답: 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'

# 조합: 서로다른 n개에서 서로다른 r개를 순서에 상관없이 선택하는것.
# 예) {'A','B','C'}에서 순서를 고려하지 않고 두개를 뽑는경우
답: 'AB', 'AC', 'BC'

'''

#순열 구하기 ================
from itertools import permutations

data= ['A','B','C'] #데이터준비
result = list(permutations(data,3))# 모든 순열 구하기
print(result)

#조합 구하기 ===============
from itertools import combinations

data=['A','B','C'] #데이터준비
result= list(combinations(data,2)) #2개를 뽑는 모든조합 구하기
print(result)

# 중복순열 구하기 ===========
print('# 중복순열 구하기 ===========')
from itertools import product

data=['A','B','C'] #데이터준비
result=list(product(data,repeat=2))#2개를 뽑는 모든 순열구하기(중복허용)
print(result)

# 중복조합 구하기 ===========
print('# 중복조합 구하기 ===========')
from itertools import combinations_with_replacement

data=['A','B','C'] #데이터준비
result=list(combinations_with_replacement(data,2))#2개를 뽑는 모든 조합 구하기(중복허용)
print(result)



'''
Counter : 등장횟수 세는 기능
'''
print('Counter : 등장횟수 세는 기능=======')

from collections import Counter

list =['red', 'blue','red','green', 'blue', 'blue']
counter = Counter(list)
print(counter) #각 요소별 중복횟수 반환. dict형으로 반환.
print(counter['red']) #red가 등장한 횟수



'''
최대공약수 / 최소공배수

'''
print('최대공약수 / 최소공배수=======')

import math

#최소공배수(lcm)
def lcm(a,b):
    return a*b // math.gcd(a,b)

a=21
b=14
#최대공약수(gcd)
cd=math.gcd(a,b)
print(cd) # 최대공약수(GCD)
print(lcm(a,b))
