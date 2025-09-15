# -----------------------------------------------------------------
# Dic 자료형 살펴보기
# - 컨테이너 타입 중 매핑 타입 => key:value
# - 형식 : {key : value, key : value, ....}
# - 특징 : key로 value를 찾음! 인덱스 필요 없음!!
# -----------------------------------------------------------------

## dict 원소 읽기/변경/추가하기

# 동일한 key의 경우, 뒤의 k : v 저장
d1 = {'name':'홍길동', 'age': 10,'jumsu':[90, 99, 100], 'rank' : 10, 'age' : 759} 
                   
print(f'd1 => {type(d1)}, {len(d1)}개, {d1}')

## dict 요소 읽기
print(f' name => {d1["name"]}')
print(f' jumsu => {d1["jumsu"]}')
print(f' 마지막 과목 jumsu => {d1["jumsu"][-1]}')

## dict 요소 변경
d1['name'] = '홍이장군'  ## 개명 '홍길동' ===> '홍이장군'
print(d1)

d1['jumsu'] = 98    ## 점수 list => int 변경
print(d1)

## dict 원소 추가 ex) 변수명[새로운키] = 값
d1["gender"] ='남자' 
d1['id'] = 'hong123'
print(d1)

## dict 원소 삭제 =>  del 변수명[key]
# rank키 삭제
del d1['rank']

# name키 삭제
del d1['name']

print(d1)