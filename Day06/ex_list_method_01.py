# --------------------------------------------------------------------
# list 타입 전용 메서드
# --------------------------------------------------------------------
## 원소/요소 추가 메서드 => append(), insert()

## append() : 리스트의 마지막에 추가 
nums=[]

nums.append("1")
nums.append(100)
print(f'원소 수 : {len(nums)}개, {nums}')

nums.append(100)
nums.append(False)
print(f'원소 수 : {len(nums)}개, {nums}')

## insert(index, data) : 원하는 위치에 데이터 추가, 젤 뒤에 추가는 안됨
## 0번 위치에 "오늘" 추가
nums.insert(0, "오늘")
print(f'원소 수 : {len(nums)}개, {nums}') # 원래 데이터는 뒤로 밀림

## 인덱스로 원소 추가 X ==> method 이용
## - 현재 원소 개수 : len(변수명)
nums[len(nums)] = 'Good Luck' ## ERROR 범위 벗어남