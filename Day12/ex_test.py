## ----------------------------------------------------------
## 함수 관련
## ----------------------------------------------------------
## [실1] 데이터의 타입에 따른 덧셈 결과를 반환하는 함수
##       함수이름은 back_result
##       매개변수는 3개의 데이터. (int, float, str)
##       타입이 다른 경우 형변화 후 결과 반환
## ----------------------------------------------------------
def back_result(data1, data2, data3) :
    ## 내장함수 isinstance(data, 타입명) => True/False 를 사용해도 됨
    if  type(data1) == str or type(data2) == str or type(data3) == str:
        d1 = str(data1)
        d2 = str(data2)
        d3 = str(data3)
        return d1+d2+d3
    else: 
        return data1+data2+data3

print(back_result(1, 2, "hello"))




## ----------------------------------------------------------
## [실2] 변환을 원하는 조건에 맞는 결과를 반환하는 함수
##       함수이름은 convert_number
##       매개변수는 정수만 가능, 진법(10진수 ,8진수, 2진수, 16진수)
##       그 외의도 처리
##       
## ----------------------------------------------------------

def convert_number(data, num) :
    if type(data) != int : return "정수값을 넣어주세요"
    if num == 10 :
        return int(data)
    elif num == 8 :
        return oct(data)
    elif num == 2 :
        return bin(data)
    elif num == 16 :
        return hex(data)
    else :
        return "진수값을 알맞게 넣어주세요"
    
print(convert_number(0x12,2))

## ----------------------------------------------------------
## [실3] 4칙 연산 결과 출력 함수(반환 x)
##       함수이름은 print_calc
##       매개변수는 list타입의 숫자데이터만 가능
## ----------------------------------------------------------
def print_calc(l) :
    check = [True if type(x) != int and type(x) != float else False for x in l]
    if sum(check) : 
        print("정수 혹은 실수만 입력해주세요") 
        return
    print(f'합 : {sum(l)}')
    print(f'차 : {abs(l[0]-l[1])}')
    print(f'곱 : {l[0] * l[1]}')
    if(l[0] == 0 or l[1] == 0):
        print("0으로 나눌 수 없음")
    else :
        print(f'나누기 : {max(l)/min(l)}')

print_calc([9,'40'])


