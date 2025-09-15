# -----------------------------------------------------------------
#                            if & for
# -----------------------------------------------------------------

## 아래의 문자열에서 숫자는 숫자끼리, 문자는 문자끼리 나누어 주세요
data = "에어컨 가격은 300만원 24개월 할부"

str_s = ""
str_d = ""

for x in range(len(data)) :
    if data[x].isalpha() :
        str_s += data[x]
    elif data[x].isdecimal() :
        str_d += data[x]

print(str_s) 
print(str_d) 