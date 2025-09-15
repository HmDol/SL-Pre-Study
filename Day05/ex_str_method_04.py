# ------------------------------------------------------------------------------------------
# str 전용 메서드 : 문자열 검사해주는 메서드 => 결과 True/False
#                  메서드명 특징 : is____()
# ------------------------------------------------------------------------------------------

## 대소문자 검사 메서드 : isupper(), islower()
print(f'{"GOOD".isupper()}')
print(f'{"GOOD".islower()}')
print(f'{"GOOD".isspace()}')

print()
## 문자 구성 요소 종류 검사 : isalpha(), isdigit()
print(f'{"GOOD".isalpha()}') # 언어 이루어짐?
print(f'{"GOOD7".isalpha()}')
print(f'{"오늘".isalpha}') # 한글도 true

## 숫자 관련 검사 : isdecimal < isdigit < isnumeric 
## but,음수, -, + 기호, 실수는 모두 false
print(f'{"1234".isdigit()}') # 10진수 + 첨자 숫자, 원형 숫자 기호 등
print(f'{"a1234".isnumeric()}') # 거의 모든 숫자 관련 기호 
print(f'{"a1234".isdecimal()}') # 10진수임?




