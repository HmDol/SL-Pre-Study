# -----------------------------------------------------------------
# Dict 전용 메서드
# ★ 필수 메서드 : keys(), values(), items()
# -----------------------------------------------------------------

## dict의 키만 가져오기 : keys()
std = {'학년':1, "반":5, '이름':'마징가', "번호":10}
keys = std.keys()
print(f'키만 추출 : {keys}, {type(keys)}, {len(keys)}')

# 인덱스 기반 접근 X
#print(keys[0]) ## type ERROR, 타입이 list가 아님

# But, list로 형 변환 후 접근 가능!
list_key = list(keys)
print(list_key[0], type(list_key))

# for ~ in 으로 접근 가능!
for k in keys:
    print(k, std[k], end='\t', sep='-')




## dict의 값만 가져오기 : values()
std = {'학년':1, "반":5, '이름':'마징가', "번호":10}

values = std.values()
print(f'values => {type(values)}, {len(values)}개, {values}')

# 값을 하나씩 출력
for v in values :
    print(v, end="\t")
print()




## dict의 (키, 값) 튜블로 묶어서 가져오는 메서드 : items()
std = {'학년':1, "반":5, '이름':'마징가', "번호":10}

items = std.items()
print(f'items => {type(items)}, {len(items)}개, {items}')

# 키와 값 읽을 경우 for ~ in 반복문
for i in items:
    print(i, end='\t')
print()

for k, v in items :
    print(k, v , end="\t")