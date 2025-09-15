# --------------------------------------------------------------------------------------
# for ~ in 반복문 : 원소 읽기용
# --------------------------------------------------------------------------------------

## list와 tuple
persons = [('홍길동', '대구'), ('마징가', '부산'), 'Good']
#          -----원소 0번----   -----원소 1번---- -원소3번-

for p in persons :
    print(p, type(p)) # tuple 타입임


 ## lsit와 언팩킹(Unpacking)   
persons = [('홍길동', '대구')]

for name, loc in persons: 
    print(name, loc, type(name), type(loc)) ## 각각 str 타입임


# --------------------------------------------------------------------------------------
# for ~ in 반복문 : 카운팅/인덱싱 용
# --------------------------------------------------------------------------------------
datas = ['1', '5', '9']

## str ==> int 형변환
datas[0] = int(datas[0])
datas[1] = int(datas[1])
datas[2] = int(datas[2])

print(datas)

## int ==> str 형변환, for in 사용
for idx in range(len(datas)):
    datas[idx] = str(datas[idx])

print(datas)