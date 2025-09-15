# --------------------------------------------------------------------------------------
# for ~ in 반복문
# --------------------------------------------------------------------------------------

## 1. 정수를 10개 입력 받아 최대값, 최소값, 평균 출력
sum = 0

list = input("정수를 입력하세요(ex. 1 2 3 4 ...) : ").split()
list.sort()

for x in list :
    sum = sum + int(x)    
print("1번")
print(f'최솟값 : {list[0]}')
print(f'최댓값 : {list[9]}')
print(f'평균 : {sum/len(list)}')



## 2. Happy 단어의 코드값을 출력하기
print("\n2번")

# for x in "Happy" :
#     print(f'{x} / {ord(x)} / {bin(ord(x))[2:]}')

ord_val = ""
bin_val = ""

for x in "Happy":
    ord_val += str(ord(x))
    bin_val += str(bin(ord(x))[2:])

print(f'Happy  {ord_val}  {bin_val}')
  