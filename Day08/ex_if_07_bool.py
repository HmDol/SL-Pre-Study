# -------------------------------------------------------
# 조건문 bool 객체
# -------------------------------------------------------
# if 조건식 : <= 조건식의 결과가 True 인지 False 체크
# -------------------------------------------------------

## int/float 타입과 bool
print(f'int타입의 경우 False인 숫자 : 0, {bool(0)}')
print(f'int타입의 경우 True인 숫자 : 0제외 나머지, {bool(-3)}')
print(f'float타입의 경우 False인 숫자 : 0.0, {bool(0.0)}')
print(f'float타입의 경우 True인 숫자 : 0.0제외 나머지, {bool(3.14)}')


## str/list/tuple 타입과 bool : 원소가 0개면 False, 나머지 True
print(f'str타입의 경우 False인 경우, 원소 0개 {bool("")}')
print(f'list타입의 경우 False인 경우, 원소 0개 {bool([])}')
print(f'tuple타입의 경우 False인 경우, 원소 0개 {bool(())}')



