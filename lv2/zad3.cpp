#include "mbed.h"

BusOut myleds(p5,p6,p7,p8,p9,p10,p11,p12);
int dec;
double increasing_factor = 2;

int main() {
    myleds=1;
    wait(0.1);
    while(1){
        dec=2;
        for(int i=0;i <6; i++){
            myleds = dec;
            dec *= increasing_factor;
            wait(0.1);
        }
        myleds = 255;
        wait(0.1);
        
        dec/=2;
        for(int i=0; i< 6; i++){
            myleds = dec;
            dec /= increasing_factor;
            wait(0.1);
        }
        myleds = 255;
        wait(0.1);
    }

}
