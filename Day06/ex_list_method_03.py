# --------------------------------------------------------------------
# list 타입 전용 메서드
# --------------------------------------------------------------------

## extend(리스트) : 리스트 합쳐서 확장
nums=[11,22,33]
nums.extend([9,8,7])
print(f'확장 후 : {nums}')

nums.extend([9,8,7])
print(f'확장 후 : {nums}')

print(f'덧셈 진행 {nums + ["a","b"]}') ## 덧셈은 원본에 추가를 위해 따로 저장을 해야됨


## remove(), pop(), clear() : 원소 삭제 관련 메서드 

## remove(데이터) :  젤 앞의 해당 데이터 원소를 삭제함(모두 삭제 x)
nums.remove(9)
print(f'삭제 후 : {nums}')

# nums.remove(100) # 해당 값 없으면 ERROR 발생

## pop() : 젤 뒤 혹은 해당 인덱스 요소를 반환 후, 삭제

nums.pop(4)
print(f'꺼낸 값 : {nums.pop()}')
print(f'pop(4) 삭제 후 : {nums}')

## clear() : 모든 요소 삭제
nums.clear()
print(f'클리어 : {nums}') 
