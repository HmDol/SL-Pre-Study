# ------------------------------------------------------------------------------------
# 메서드(Method) 이해
# - 특정 데이터 타입에서만 사용가능한 함수, 전용함수
# - 일반 모든 타입에서 사용되는 함수와 구별됨
# - ex) 일반 함수 : print('hello')
# -     매 서 드 : 객체변수명.메서드()
# ------------------------------------------------------------------------------------

## str타입 객체 생성
msg = "Good Luck 2020!"

## str타입의 메서드 사용
## 1. 요소 변경 메서드 : replace(old, new, count=-1)
msg = msg.replace("G",'g')
print(msg)

msg = msg.replace("o",'*')
print(msg)

msg = msg.replace("0",'5')
print(msg)

msg = msg.replace("*",'O', 1) # 앞에서 부터 1개만 바꿈
print(msg)

msg = msg.replace("*",'O', 0) # 0개 변경 즉, 변경X
print(msg)


print()
## 2. 대소문자 관련 메서드 : upper(), lower(), swapcase()
msg = "HEllo"

print("모두 대문자 : ", msg.upper())
print("모두 소문자 : ", msg.lower())
print("대 <-> 소 바뀜 : ",msg.swapcase() )
# msg = msg.upper() # 저장


