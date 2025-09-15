# ---------------------------------------------------------
# for ~ in 반복문과 enumerate 객체
# ---------------------------------------------------------

## enumerate() : 원소와 인덱스를 함께 반환
nums = list('Merry Christmas')

## 원소를 정수로 바꿔서 저장
for idx in range(len(nums)):
    nums[idx] = ord(nums[idx])

print(nums)

## enumerate()
nums = list('Merry Christmas')

for idx, num in enumerate(nums):
    nums[idx] = ord(nums[idx])
    print(idx, num, nums[idx])