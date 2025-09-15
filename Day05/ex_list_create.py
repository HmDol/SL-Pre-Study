# ----------------------------------------------------------------
# 컨테이너 자료형 : 여러개의 데이터를 저장하는 자료형
# -> 그 중 순서 있는 자료형 : 시퀀스(Sequence) 자료형
# ----------------------------------------------------------------

## 1. List 자료형 
## - 형식 : [데이터, 데이터, 데이터, .... , 데이터] / 빈 리스트도 존재

data= []
print(data, type(data), len(data))

data = list([])           ## 생성자(constructor) : 빈 리스트 생성
print(data, type(data), len(data))       ## list 자료형과 동일한 이름의 함수

data = [1,3,9]          ## data = list([1,3,9]) 가 원래 형식
print(data, type(data), len(data))

data = [False, 'Good', 4.9, 7]          
print(data, type(data), len(data))

data = [False, 'Good', 4.9, 7, []] # 이중 리스트 가능
print(data, type(data), len(data))



