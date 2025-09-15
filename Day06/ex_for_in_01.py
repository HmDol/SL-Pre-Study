# -----------------------------------------------------------------------
# for in 반복문 : 원소를 하나씩 읽어오기 위해 사용
# -----------------------------------------------------------------------
msg = "Happy New Year! Merry christmas~ Good Luck 2025"

## 요청 : str에서 원소 하나씩 꺼내서 코드값을 출력하세요
## 변수에 저장해줌
for x in msg : 
    print(x, ord(x))

## 요청 : 입력 받은 정수 10개를 int형으로 변환
nums = input('10개 정수 입력 ex) 9 2 1 6 : ').split()

## list의 str 요소를 int로 형변환
## 이런식이면 list 수정은 안됨
for x in nums:
    print(int(x), type(int(x)))


## for로 list 수정
## 인덱스를 반복문으로 차례대로 받음
for x in range(0,len(nums)):
    nums[x] = int(nums[x])

print(nums) ## 정수형태의 원소로 바뀜


