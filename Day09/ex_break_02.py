# -------------------------------------------------------------------
# break : 반복문을 즉시 중단하는 명령어
#          - 따라서 break 아래의 코드는 실행 안됨!
#          ★ 중첩 반복문의 경우 break와 가까이 있는 반복문만 중단됨
# -------------------------------------------------------------------


## 요청. 중첩 반복문과 break
isstop = False ## flag 체크 변수

for ch in "ABCDEFGHIJZKLMN":
    print(ch)
    for num in range(4,20):
        if num == 11 : 
            isstop = True
            break
        print(num)

    ## 종료 조건 : 안쪽 for문 중단되면 함께 중단
    if isstop : 
        break