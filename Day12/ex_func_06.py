# ---------------------------------------------------------
# 사용자 정의 함수 : 매개변수 개수 가변 함수
#                  가변인자 함수
#                  ★일반 매개변수와 가변매개변수가 혼합 가능
# - 형식 : def 함수명(*매개변수)
# - 의미 : 0~n개 전달받음
# ---------------------------------------------------------

## 함수기능: 0개 이상 정수 덧셈 수행
## 함수이름: plus_nums
## 매개변수: num1, ... ,numN
##         *nums(아스타리크) : 0개 ~ n개 매개변수
## 반환결과: 덧셈 결과값

## 매개 변수 개수 변화에 대응하는 하나의 함수?
def plus_nums(*nums) :
    # print(type(nums)) ## 튜플 형식으로 넘어옴
    ## int, float이 아니면 계산 불가
    for x in nums :
        if type(x) not in [int, float, bool] :
            return "연산불가"
    
    return sum(nums)
    
## 함수 사용하기 => 함수 호출
print("plus_nums(1,2,4,5,6,7,7)", plus_nums(1,2,4,5,6,7,7))
print("plus_nums(False, True)", plus_nums(False, True))
print("plus_nums()", plus_nums())
