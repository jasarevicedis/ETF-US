/* mbed Microcontroller Library
 * Copyright (c) 2019 ARM Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"
#include "lpc1114etf.h"
DigitalOut enable(LED_ACT);

DigitalIn button(P0_8);
DigitalOut led[8] = {p5,p6,p7,p8,p9,p10,p11,p12};

int main()
{
    enable = 0;
    int brojac=0, b=1, inkrement = 1;
    while(1){
        b=1;
        for(int i=0;i<8;i++){
            if(b & brojac)
                led[i] = 1;
            else led[i] =0;
            b<<= 1;
        }
        printf("%d\n", brojac);
        wait_us(100000);
        if(button.read())
            brojac--;
    }
}
