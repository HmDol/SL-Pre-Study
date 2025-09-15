# --------------------------------------------------------------------
# list 타입 전용 메서드
# --------------------------------------------------------------------
## 원소/요소 인덱스 반환 메서드 => index() 

## index() : 있으면 인덱스 반환, 없으면 ERROR
## rindex() : 오->왼 방향으로 찾음
nums = list("Good Luck") # 쪼개서 들어감
print(f'원소 수 : {len(nums)}개, {nums}')

loc = nums.index("o")
print(f'첫번째 o 인덱스 : {loc}')
loc = nums.index("o", loc+1)
print(f'두번째 o 인덱스 : {loc}')

## count() : 해당 원소/요소 개수 가져오는 메서드
print(f'o 원소의 수 : {nums.count("o")}')
print(f'k 원소의 수 : {nums.count("k")}')

## reverse() : 원소를 역으로 뒤집어서 저장 메서드, 정렬x
nums = [10, 2, 5, 9, 3, 7]
print(f'순방향 : {nums}')
nums.reverse() # 리턴값 x, 원본이 바뀜
print(f'역방향 : {nums}')


## sort() : 원소 정렬 후 저장하는 메서드
## 기본 : 오름차순(작->큰)
nums.sort()
print(f'정렬 후 : {nums}')


## 내림차순(큰->작) 정렬
nums.sort(reverse=True)
print(f'내림 정렬 후 : {nums}')