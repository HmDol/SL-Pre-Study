/*
변수 선언 및 초기화
*/

#include <stdio.h>

void main()
{
    // 변수 선언
    int age;
    int year;
    int month = 9;
    int day = 18;

    // 초기화x => 정크 값들이 들어가 있음
    print('[before] age : %d, year : %d, month : %d, day : %d\n', age, year, month, day);

    // 변수 초기화
    age = 26;
    year = 2025;
    

    print('[before] age : %d, year : %d, month : %d, day : %d\n', age, year, month, day);
}