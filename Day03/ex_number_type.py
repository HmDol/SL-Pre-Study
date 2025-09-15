# -------------------------------------------------------------------------
# 숫자 표기법 : 2진수, 8진수, 16진수 변환
# -------------------------------------------------------------------------
# 진수 변환 내장함수 => bin(), oct(), hex(), int()

noDec = 2025
noBin = '0b111' # 진수들은 모두 문자열 처리
noOct = '0o7'
noHex = '0x15'

## 10진수 -> 진수 변환
print(f'{noDec}  2진수 변환 : {bin(noDec)}')
print(f'{noDec}  8진수 변환 : {oct(noDec)}')
print(f'{noDec} 16진수 변환 : {hex(noDec)}')

print()
## 2/8/16 진수 => 10진수 변환 (wjdt)
print(f'{noBin} 10진수 변환 : {int(noBin, base=0)}') # base : 데이터가 몇 진수인지 적기 (0 = 2)
print(f'{noBin} 10진수 변환 : {int(noBin, base=2)}') 
print(f'{noOct} 10진수 변환 : {int(noOct, base=8)}')
print(f'{noHex} 10진수 변환 : {int(noHex, base=16)}')


