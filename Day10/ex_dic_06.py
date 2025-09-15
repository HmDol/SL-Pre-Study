# -----------------------------------------------------------------
# Dict 전용 메서드
# -----------------------------------------------------------------
 
## 원소 추가/갱신 메서드 : get(key, default)
## - 키가 없을 경우 default값을 반환
jumDict = {'과목1': 98, "과목2" : 99, "과목3":100, "과목4":78, "과목5":88}

# => 값 가져오기
print(f'{jumDict["과목1"]}')
# print(f'{jumDict["과목11"]}') ## 키 없음 ERROR

# => get() 메서드
print(jumDict.get('과목1'))
print(jumDict.get('과목11',"존재하지 않는 과목"))
print(jumDict.get('과목11',0))




## 원소 꺼내기 : pop()
## - 꺼내진 원소는 값을 반환
## - 꺼내진 원소는 삭제
print(jumDict.pop('과목1'))
print(jumDict)

print(jumDict.pop('과목11',"존재하지 않는 과목"))
print(jumDict)



## 원소 꺼내기 : popitem()
## - dict의 마지막 원소를 (키, 값) 꺼내기
## - dict에서 제거됨

print(jumDict.popitem())
print(jumDict)



## 원소 모두 삭제 : clear()
jumDict.clear()
print(jumDict)