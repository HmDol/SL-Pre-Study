/*
데이터 타입 - 정수형
메모리 낭비를 막기 위해서 다양한 종류 존재
- 2byte(2칸) : short
- 4byte(4칸) : int
- 4byte(4칸) : long
- 8byte(8칸) : long long
*/


#include <stdio.h>

int main()
{
    short sh = 12;        // short 정수형 변수
    int nt = 155;         // int 정수형 변수
    long long on = 1666;  // long long 정수형 변수

    //sizeof() : 메모리 할당량을 반환한다
    printf("자료형의 크기를 알아보는 코드 \n");
    printf("1. short : %dbyte, %dbyte \n", sizeof(sh), sizeof sh);
    printf("2. int   : %dbyte, %dbyte \n", sizeof(nt), sizeof nt);
    printf("3. long long : %dbyte, %dbyte \n", sizeof(on), sizeof on);
    printf("4. float : %dbyte \n", sizeof(float));

    return 0;
}
