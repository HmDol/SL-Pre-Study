# ---------------------------------------------------------------
# Comprehension => list, dict, set
# ---------------------------------------------------------------
# 형식 : for in     +   if else   +      list/dict/set
# ---------------------------------------------------------------

## List comperhension
## str 타입의 숫자를 int타입의 숫자로 형변환
nums = ["9", "0", '4', "7", "2"]
list = []

# 일반 방식
for x in nums :
    list.append(int(x))
print(list)

# comprehension 방식
res = [int(x) for x in nums]
print(res)


## Dict comprehension
## 문자에 대한 코드값 저장된 chr2code => 코드값에 대한 문자값
## chr2code = {'A' : 65, "C" : 67, "b" : 98}
chr2code = {'A' : 65, "C" : 67, "b" : 98, '3' : 3}
code2chr={}

# 일반 방식
for k,v in chr2code.items():
    code2chr[v] = k
print(code2chr)

## comprehension 방식 : 모든 원소
## => 방법1 dict comprehension : 모든 원소
res = {v : k for k,v in chr2code.items()}
print(res)

## => 방법2 - dict comprehension : 필터링
## 대문자 문자만 코드값 저장
res = {v : k for k,v in chr2code.items() if k.isupper()}
print(res)


## => 방법3 - dict comprehension : 원소마다 다른 저장법 적용
## key 가 str 숫자는 k와 v 변경 없이 그대로
## key가  문자이면 k v 교체
res = { (v if k.isalpha() else k): (k if k.isalpha() else v) for k, v in chr2code.items()}
print(res)


## Set comprehension
## "Good Luck" 데이터에서 중복된 문자는 1번만 저정
del list
msg1 = list("Good Luck")
msg2 = set("Good Luck")
msg3 = {ch for ch in "Good Luck"}

print(f'msg1 : {msg1}')
print(f'msg2 : {msg2}')
print(f'msg3 : {msg3}')

## 중복x, 특정 데이터 필터링 => 소문자만 저장
msg4 = {ch for ch in "Good Luck" if ch.islower()}
print(f'msg4 : {msg4}')