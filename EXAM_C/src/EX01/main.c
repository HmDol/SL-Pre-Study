/*
여러줄 주석입니다.
*/

#include <stdio.h>

/*
Entry Point
*/
int main(){
    printf("Hello World!\n");
    // %s : 문자열
    // %c : 단일 문자
    printf("정수 %d , 실수 %f, 문자 %c , 문자열 %s", 2025, 4.0, 'F', "안녕하세요");
    printf('Alert \a');
    return 0;
}