CC = gcc
CFLAGS = -lkovan -lm -lpthread -include kovan/kovan.h -include stdio.h -include target.h -include math.h
OBJFLAGS = -c -Wall -Werror -fpic
SOFLAGS = -shared


libControl.so : Control.o
	$(CC) $(CFLAGS) $(SOFLAGS) -o libControl.so Control.o
Control.o : Control.c
	$(CC) $(CFLAGS) $(OBJFLAGS) Control.c
clean:
	rm -rf *.o
	rm -rf *.so
script:
	./librarycompile.sh
