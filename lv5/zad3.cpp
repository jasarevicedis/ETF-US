/* mbed Microcontroller Library
 * Copyright (c) 2019 ARM Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"

#define WAIT_TIME_MS 5
DigitalOut led1(LED1);
AnalogOut out(PTE30);

int main()
{
    printf("This is the bare metal blinky example running on Mbed OS %d.%d.%d.\n", MBED_MAJOR_VERSION, MBED_MINOR_VERSION, MBED_PATCH_VERSION);

    float brojac = 1;
    float var = 0;
    //out.period_us(50);
    while (true)
    {
        var = brojac / 50.;
        
        out.write(var);
        brojac +=0.9;
        wait_ns(50);
        //thread_sleep_for(WAIT_TIME_MS);
        if(brojac > 50) brojac = 1;
        
    }
}
