# s = input()
s="one4seveneight"

alpa=['one','two','three','four','five','six','seven','eight','nine','zero']
nums=['1','2','3','4','5','6','7','8','9','0']
# newS =[] #새로운 리스트
def solution(s):
    for a in alpa:
        if a in s :
            # print ("있어! ", a) #문자열 찾기
            pos=alpa.index(a) #문자열 리스트에서 해당 인덱스 찾기
            # print(pos, '숫자로 ->', nums[pos])
            newS=s.replace(a,nums[pos])
            s=newS
            # print(newS)

    # answer = newS
    s = int(s)
    print(type(s))
    answer = s
    return answer

print(solution(s), type(solution(s)))
