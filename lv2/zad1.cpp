#include "mbed.h"

DigitalOut leds[] = {(LED1), (LED2), (LED3), (LED4)};

/*
DigitalOut myled1(LED1);
DigitalOut myled2(LED2);
DigitalOut myled3(LED3);
DigitalOut myled4(LED4);*/

int main() {
    
//first version of code
    /*
    while(1) {
        myled = 1;
        wait(1);
        myled = 0;
        wait(1);
    }*/
//modified code
    while(1) {
        for(int i = 0; i<=3; i++){
            leds[i] = 1;
            wait(1);
            leds[i] = 0;
            wait(1);
        }
    }
}
