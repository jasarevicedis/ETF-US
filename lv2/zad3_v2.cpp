/* mbed Microcontroller Library
 * Copyright (c) 2019 ARM Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"
#include "lpc1114etf.h"

BusOut myleds(P0_0,
       P0_1,
       P0_2,
       P0_3,
       P0_4,
       P0_5,
       P0_6,
       P0_7);
int dec;
double increasing_factor = 2;
DigitalOut enable(LED_ACT);

int main() {
    enable = 0;
    myleds=1;
    wait_us(100000);
    while(1){
        dec=2;
        for(int i=0;i <6; i++){
            myleds = dec;
            dec *= increasing_factor;
            wait_us(100000);
        }
        myleds = 255;
        wait_us(100000);
        
        dec/=2;
        for(int i=0; i< 6; i++){
            myleds = dec;
            dec /= increasing_factor;
            wait_us(100000);
        }
        myleds = 255;
        wait_us(100000);
    }

}
