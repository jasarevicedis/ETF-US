#include "mbed.h"

DigitalOut led1(LED1);


void light_time_changing(double T){
    double T_change_const = 0.9/30.0;
    double on_period = T;
    double off_period = T;
    
//RANGE CONSTANTS, for avoiding calculating in while loop condition
    double MAX_TIME =1.9*T;
    double MIN_TIME =0.1*T;
    
    for(;;){
        led1 = 1;
        wait(on_period);
        led1 = 0;
        wait(off_period);
        if(on_period < MAX_TIME){
            on_period += T_change_const;
            off_period -= T_change_const;
        }
        else 
            break;
    }
    //to not repeat latest step
    on_period -= T_change_const;
    off_period += T_change_const;
    for(;;){
        led1 = 1;
        wait(on_period);
        led1 = 0;
        wait(off_period);
        if(on_period > MIN_TIME){
            on_period -= T_change_const;
            off_period += T_change_const;
        }
        else 
            break;
    }
    
}

int main() {
    while(1){
        light_time_changing(1);
    }
}
