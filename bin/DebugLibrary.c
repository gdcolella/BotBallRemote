#include <stdio.h>



void lib_motor(int v0 ,int v1 ){
	printf("motor  %d  %d \n", v0,v1);
}



void lib_mav(int v0 ,int v1 ){
	printf("mav  %d  %d \n", v0,v1);
}



void lib_msleep(int v0 ){
	printf("msleep  %d \n", v0);
}



void lib_freeze(int v0 ){
	printf("freeze  %d \n", v0);
}













void lib_set_servo_position(int v0 ,int v1 ){
	printf("set_servo_position  %d  %d \n", v0,v1);
}



void lib_create_connect(){
	printf("create_connect \n" );
}



void lib_create_disconnect(){
	printf("create_disconnect \n" );
}



void lib_create_drive_direct(int v0 ,int v1 ){
	printf("create_drive_direct  %d  %d \n", v0,v1);
}



void lib_enable_servos(){
	printf("enable_servos \n" );
}



void lib_ao(){
	printf("ao \n" );
}

