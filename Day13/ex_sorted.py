# --------------------------------------------------
# 내장함수 filter()
# - 형식 : sorted(함수이름, iterable)
# - 기능 : 정렬 (기본: 오름차순) 후, 리스트 반환
# --------------------------------------------------

## list 타입의 iterable 데이터 -----------------------
data = [2,2,5,7,4,2,1,8,9,6,4,3]

asc = sorted(data)              ## 오름차순
dec = sorted(data,reverse=True) ## 내림차순

print(f'asc : {asc}')
print(f'dec : {dec}')
print()

## tuple 타입의 iterable 데이터 -----------------------
data = (2,2,5,7,4,2,1,8,9,6,4,3)

asc = sorted(data)              ## 오름차순
dec = sorted(data,reverse=True) ## 내림차순

print(f'asc : {asc}') ## 리스트로 반환
print(f'dec : {dec}') ## 리스트로 반환
print()

## set 타입의 iterable 데이터 -----------------------
data = {2,2,5,7,4,2,1,8,9,6,4,3} 

asc = sorted(data)              ## 오름차순
dec = sorted(data,reverse=True) ## 내림차순

print(f'asc : {asc}') ## 리스트로 반환
print(f'dec : {dec}') ## 리스트로 반환
print()

## dict 타입의 iterable 데이터 -----------------------
data = {"A": 10, 'Z' : 7, "D" : 20, "B": 100}

# key 위주
asc = sorted(data)              ## 오름차순
dec = sorted(data,reverse=True) ## 내림차순

print(f'asc : {asc}') ## Key만 리스트로 반환
print(f'dec : {dec}') ## Key만 리스트로 반환
print()

# value 위주
# (k,v) : items() ==> [0] : key1, [1] : value1
# key =에 각 튜플(items)의 value값을 넣는거                      
asc = sorted(data.items(), key=lambda item : item[1])      ## 오름차순
dec = sorted(data.items(),reverse=True, key=lambda item : item[1]) ## 내림차순

print(f'asc : {asc}') ## value 기준 정렬
print(f'dec : {dec}') ## value 기준 정렬
print()

## => sorted() 내장함수의 정렬 기준 설정 => key 매개변수 -----------------
data = ['Good', 'apple', 'Zoo', 'banana']

# 코드값 기준
asc = sorted(data)
dec = sorted(data, reverse=True)
print(f'asc : {asc}') 
print(f'dec : {dec}') 
print()

# 문자 길이 기준
asc = sorted(data,key = lambda s : len(s))
dec = sorted(data, reverse=True, key = lambda s : len(s))
print(f'asc : {asc}') 
print(f'dec : {dec}') 
print()

# abc 기준 (소문자로 통일)
asc = sorted(data,key = lambda s : s.lower())
dec = sorted(data, reverse=True, key = lambda s : s.lower())
print(f'asc : {asc}') 
print(f'dec : {dec}') 
print()






