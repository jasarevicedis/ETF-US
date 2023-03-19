#include "mbed.h"

BusOut myleds(p5,p6,p7,p8,p9,p10,p11,p12);
DigitalIn mybutton(BUTTON1);

int counter = 1;
int adding_factor = 1;

int main() {
    while(1){
        if()
        myleds = counter;
        counter += adding_factor;
        wait(1);
    }

}
