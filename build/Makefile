SRC = ../src
DST = ../upload


all :
	rm -f $(DST)/*
	python GenerateCommands.py
	cp $(SRC)/Control.c $(DST)
	cp $(SRC)/Makefile  $(DST)
	cp $(SRC)/networkHandler.py $(DST)
