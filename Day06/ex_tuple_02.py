# ------------------------------------------------------------------------------
# 순서있는(Sequence) 자료형 - touple
# - 변경 혹은 수정을 위해 list로 형변환
# - tuple -> list 형변환 -> 수정 및 삭제 -> tuple 형변환
# ------------------------------------------------------------------------------

phone=('011','016','017','018','019')

print(f'phone : {type(phone)}, {len(phone)}개, {phone}')

## list로 형변환
phone = list(phone) 
phone[:] = ['010']

print(f'phone : {type(phone)}, {len(phone)}개, {phone}')

## 다시 tuple로 형변환
phone = tuple(phone)
print(f'phone : {type(phone)}, {len(phone)}개, {phone}')
