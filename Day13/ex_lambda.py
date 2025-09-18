# --------------------------------------------------
# 다양한 lambda 사용법
# --------------------------------------------------
## 변수 1개 사용하는 lambda 표현식/함수
print((lambda x, y : x + y )('4','6'))
res = (lambda x, y : x + y )('4','6')
three = (lambda x, y,z  : x + y + z )('4','6','8')

## lambda 표현식/함수 코드 전에 선언된 변수 사용
y = 100
print((lambda x: x+y)(5)) ## 문제 없음

## 매개변수 없는 lambda 표현식 
(lambda : 100)() ## 100 반환


## map() + lambda + 조건부 표현식 
## 3의 배수는 str타입으로 변환, 나머지 숫자는 float으로 변환 후 저장
a = range(15)

l = list(map(lambda x : str(x) if x%3 == 0 else float(x),a))
print(l)