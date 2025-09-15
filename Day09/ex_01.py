# -----------------------------------------------------------------------
# list comprehension
# -----------------------------------------------------------------------

## str타입 메서드
# str.capitalize() : 첫글자만 대문자 나머지 소문자


data = ['apple', 'HAPPY', 'Good', 'luck']
print(f'data : {data}')

## 요청1. 새로운 리스트에 모든 원소값을 대문자로 저장하기
res = [d.upper() for d in data]
print(f'요청1 : {res}')

## 요청2. 새로운 리스트에 원소가 islower() 면 대문자, isupper()이면 소문자로 변경
res = [ d.upper() if d.islower() else d.lower() if d.isupper() else d for d in data]
print(f'요청2 : {res}')


## 요청3. 아래 데이터를 새로운 리스트에 int로 저장
data = ['3', '-1', '9', '0']
res = [int(d) for d in data]
print(f'요청3 : {res}')

## 요청4. 아래 데이터에서 숫자만 다른 리스트에 저장하기
data = "Good 2025 Happy Day 2026"
res = [d for d in data if d.isdecimal()]
print(f'요청4: {res}')