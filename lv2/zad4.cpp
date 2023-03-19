#include "mbed.h"

DigitalOut led0(p15);
DigitalIn Taster_1(p5);
DigitalIn Taster_2(p6);
BusOut myleds(p7,p8,p9,p10,p11,p12,p13,p14);

void RunningLight(double time_stamp){
    int dec;
    double increasing_factor = 2;
    
    myleds=1;
    wait(time_stamp);
    //only one ciclus is needed, so we delete while loop
        dec=2;
        for(int i=0;i <6; i++){
            myleds = dec;
            dec *= increasing_factor;
            wait(time_stamp);
        }
        myleds = 255;
        wait(time_stamp);
        
        dec/=2;
        for(int i=0; i< 6; i++){
            myleds = dec;
            dec /= increasing_factor;
            wait(time_stamp);
        }
        myleds = 255;
        wait(time_stamp);
    
}

int main() {
    while(1){
        while(Taster_1 == 0 && Taster_2 == 0){
            led0=1;
            wait(0.5);
            led0=0;
            wait(0.5);
        }
        if(Taster_1 == 1){
            RunningLight(0.1);
            myleds=0;
        }
        else {
            RunningLight(0.5);
            myleds=0;
        }
    }
    
}
