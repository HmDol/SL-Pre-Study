# ---------------------------------------------------------
# return 키워드
# - for/while 반복문 중단
# - 함수 종료 기능
# - 즉시 종료!!!
# ---------------------------------------------------------

## 반복문과 return 
for ch in 'Good Luck 2025!!':
    if ch.isspace():
        break
    print(ch)

# for ch in 'Good Luck 2025!!':
#     if ch.isspace():
#         return
#     print(ch)

print('End')

## 함수와 return 
def add(a,b):
    if b < 0 :
        return
    elif a < 0:
        return 
    total = a + b
    return total

print(add(3,2))
print(add(-1,3999))


## 함수와 반복문과 return 
# 기능 : 전달 받은 뭊자열을 한개씩 한 행에 출력
def print_row(msg) :
    for ch in msg :
        if ch.isspace() : 
            # break ## 반복문만 종료
            return ## 반환 및 함수 종료
        print(ch)
    print("-------^^----------")

print(print_row("Good Luck"))
