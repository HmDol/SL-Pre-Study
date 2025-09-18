/*
      데이터 타입
정수의 다양한 표현법/진법
2진수 => 0b0101
8진수 => 065
16진수 => 0x23A
*/
#include <stdio.h>

void main()
{
    //숫자의 다양한 진법 표시
    int binValue = 0b1001;
    int otaValue = 067;
    int hexValue = 0x1F;
    int decValue = 91;
    
    // %d : 10진수 표현, %o : 8진수로 표현, %x : 16진수로 표현, 
    printf("binValue => %d, %o, %x \n",binValue,binValue,binValue);
    printf("otaValue => %d, %x \n",otaValue,otaValue);
    printf("hexValue => %d, %o \n",hexValue,hexValue);
    printf("decValue => %d, %o, %x \n",decValue,decValue,decValue);
    
    
}