/*
데이터 타입 - 정수형
타입별 저장이 가능한 범위가 정해져 있음
해당 범위를 넘을 경우 : overflow / underflow
*/


#include <stdio.h>

int main()
{
    //범위를 넘어가면 범위가 순환됨 **주의!! : 오류가 나지 않음!
    short sMinNum = -32769; // 출력 : 32767
    short sMaxNum = 32768;  // 출력 : -32768
    float fNum = 1.8f;
    
    printf("sMinNum : %d, sMaxNum : %dm fNum : %f\n", sMinNum, sMaxNum,fNum);
    
    

    return 0;
}
