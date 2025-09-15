# -------------------------------------------------------------------------
# break / continue / pass
# -------------------------------------------------------------------------
data = "Happy!Good"
## 1. "Happy!Good" 데이터에서 원소를 옆으로 출력하세요
##      단, 문자가 아니면 중단하세요

for x in data :
    if not x.isalpha() : break
    print(x, end ="")

print()
## 2. "Happy!Good" 데이터에서 원소르 옆으로 출력하세요
##      단, 문자만 출력하세요

for x in data :
    if not x.isalpha() : continue
    print(x, end="")
print()


## while 이용 **유의해야됨
idx = -1             ## 인덱스 변수
stop = len(data)     ## 인덱스 범위 지정을 위한 변수
while idx < stop-1 :
    idx+=1
    if not data[idx].isalpha() : continue
    print(data[idx], end="")
    

