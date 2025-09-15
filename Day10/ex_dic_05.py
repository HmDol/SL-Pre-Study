# -----------------------------------------------------------------
# Dict 전용 메서드
# ★ 필수 메서드 : keys(), values(), items()
# -----------------------------------------------------------------
 
## 원소 추가/갱신 메서드 : update()
jumDict = {'과목1': 98, "과목2" : 99, "과목3":100, "과목4":78, "과목5":88}
infoDict = {'이름': '홍길동', '학년':1, "반":5}
# => 추가
jumDict.update({'과목6':100}) ## 키 값이 없다면 추가
jumDict.update({'과목6':80, '등수':3}) ## 키 값이 있다면 값 변경
print(f'jumDict => {jumDict}')

## ==> 추가
jumDict.update(infoDict) ## dict타입 추가 가능
print(f'jumDict => {jumDict}')

# ==> 추가 update(key1=value1, key2=value, ....)
#         but! key는 str만 가능하고 "",'' x
jumDict.update(국적='대한민국', 전화='010-1111-2222')
print(f'jumDict => {jumDict}')

