# --------------------------------------------------
# 내장함수 filter() : 사용법 map()과 동일
# - 형식 : filter(함수이름, iterable)
# - 기능 : 함수결과가 True인 원소만 반환
# --------------------------------------------------

## 짝수만 저장
data = [1,2,3,4,5,6,7,8,9,10]

## 방법1. for in 반복문 + 조건물
data2 = []
for d in data:
    if not d%2:
        data2.append(d)

for d in data:
    if d%2: continue
    data2.append(d)

for d in data2[2::2] : 
    data2.append(d)

# [방법2] list comprehension
data1 = [ d for d in data if d%2==0 ]


# 방법3. 내장함수 filter(함수이름, iterable)
def isvalid(d) : 
    return not d%2

print('data3 =>', list(filter(isvalid, data))) ## 참값만 반환

print('data4 =>', list(filter(lambda d : not d%2, data)))


    