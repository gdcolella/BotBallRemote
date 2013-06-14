#include <stdio.h>
#include <stdlib.h>

int main()
{
printf("Starting network server...\n");
system("python /kovan/network/networkHandler.py");
printf("Terminating server..\n");
return 0;
}
