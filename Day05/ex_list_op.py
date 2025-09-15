# ----------------------------------------------------------------
# 컨테이너 자료형 : 여러개의 데이터를 저장하는 자료형
# -> 그 중 순서 있는 자료형 : 시퀀스(Sequence) 자료형
# ----------------------------------------------------------------

## List 자료형과 연산자
data1 = [11, 22, 33, 44, 55]
data2 = ['a', 'b', 'c']

## 산술 연산자 => 덧셈 : list + list
print(data1 + data2)

# print(data1 + list(100)) # ERROR : 기본타입 => 컨테이너 타입 형변환X
# print(data1 + list(100.4/)) # ERROR
# print(data1 + list(False)) # ERROR

print(data1 + list("str")) # 컨테이너 타입은 가능 

## 산술 연산자 => 곱셈 : list * 정수
print(data1 * 3)


## 맴버 연산자 => 원소/요소가 맞는가 검사  in/not in
dataList = [ 11, 14, "apple", 'summer', False]

print(f'11 in dataList : {11 in dataList}')
print(f'apple in dataList : {"apple" in dataList}')
