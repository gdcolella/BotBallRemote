

void test(){
	printf("Working.. probably\n");
}

void lib_mav(int mtrnum, int v){
mav(mtrnum,v);
}

void lib_ao() {
ao();
}

void lib_motor(int mtrnum, int power){
motor(mtrnum,power);
}

void lib_msleep(int ms){
msleep(ms);
}

void lib_enable_servos(){
	enable_servos();
}
void lib_disable_servos(){
	disable_servos();
}

void lib_set_servo_position(int servo, int position){
	set_servo_position(servo,position);
}

void lib_create_connect(){
	create_connect();
}

void lib_create_drive_direct(int left, int right){
	create_drive_direct(left,right);
}

void lib_create_disconnect(){
	create_disconnect();
}

void lib_freeze(int motor){
	freeze(motor);
}

