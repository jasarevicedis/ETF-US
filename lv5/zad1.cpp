/* mbed Microcontroller Library
 * Copyright (c) 2019 ARM Limited
 * SPDX-License-Identifier: Apache-2.0
 */


#include "mbed.h"
#include "lpc1114etf(6).h"

PwmOut led(dp18);

BusOut myleds(P0_0,
       P0_1,
       P0_2,
       P0_3,
       P0_4,
       P0_5,
       P0_6,
       P0_7);
DigitalOut enable(LED_ACT);


AnalogIn ain(dp9);
int main() {
    myleds = 0;
    enable = 0;
    while(1){
        led.period_us(50);
        led = ain;
        //wait_us(100000);
        
    }
    

}
