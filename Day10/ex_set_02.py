# -----------------------------------------------------------------
# Set 자료형 전용 메서드
# - add() : 한개 원소 추가
# - update( iterator ) : 여러개 원소 추가
# - remove() : 원소 삭제 
# -----------------------------------------------------------------

## set 객체 생성
s1 = set({1,1,3,5,7,7}) ## 빈 집합 생성
print(f's1 => {type(s1)}, {len(s1)}개, {s1}')


# 원소 추가
s1.add(100)
s1.add('Happy')
s1.add(5)
print(f's1 => {type(s1)}, {len(s1)}개, {s1}')


# 여러개 추가 (iterable 타입만 추가 가능)
s1.update([1,9,9,'B'])
print(f's1 => {type(s1)}, {len(s1)}개, {s1}')

s1.update("ABCDEF")
print(f's1 => {type(s1)}, {len(s1)}개, {s1}')


# 삭제
s1.remove(1)
print(f's1 => {type(s1)}, {len(s1)}개, {s1}')

print(f'있음 : {"A" in s1}')
# s1.remove(1) ## key ERROR , 이미 없음
print(f's1 => {type(s1)}, {len(s1)}개, {s1}')



## 중복 제거
nums = [1,2,1,12,2,12,2,2,1,1,12,5,7,6,5,4,6,7]
s = list(set(nums))
print(s)
