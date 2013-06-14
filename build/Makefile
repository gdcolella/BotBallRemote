SRC = ../src
DST = ../bin
CC = gcc
OBJFLAGS = -c -Wall -Werror -fpic
SOFLAGS = -shared


all :
	rm -rf $(DST)
	mkdir $(DST)
	python GenerateCommands.py
	python GenerateLibrary.py
	cp $(SRC)/Control.c $(DST)
	cp $(SRC)/Makefile  $(DST)
	cp $(SRC)/networkHandler.py $(DST)
	cp $(SRC)/ServerRunner.c $(DST)
	$(CC) $(CFLAGS) $(OBJFLAGS) $(DST)/DebugLibrary.c -o $(DST)/DebugLibrary.o
	$(CC) $(CFLAGS) $(SOFLAGS) -o $(DST)/libDebug.so $(DST)/DebugLibrary.o
	chmod +x $(DST)/networkHandler.py


clean : 
	rm -rf $(DST)
