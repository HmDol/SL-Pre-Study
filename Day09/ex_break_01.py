# -------------------------------------------------------------------
# break : 반복문을 즉시 중단하는 명령어
#          - 따라서 break 아래의 코드는 실행 안됨!
# -------------------------------------------------------------------

## 요청. data리스트의 원소가 7의 배수면 중단
data = [1,3,5,7,9,11,13]

for d in data:
    if d%7 == 0 : break
    print(d)

idx = 0
size = len(data)
print()
while idx < size :
    if not data[idx]%7 : break
    print(data[idx])
    idx += 1