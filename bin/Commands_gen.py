#!/usr/bin/env python
import sys
import socket
import time
from ctypes import cdll

class Command:
	def create_from(self,argarray):
		return
	def execute(self):
		return
	def toCommands(self):
		return ''


class mtr_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
                self.v0 = argarray[0]
                
                self.v1 = argarray[1]
                
		return

        def execute(self):
                
                self.lib.lib_motor(self.v0,self.v1)
                
		return

        def toCommands(self):
                out = ""
		
		out+="motor("+str(self.v0)+","+str(self.v1)+");\n"
		
		return out

class mav_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
                self.v0 = argarray[0]
                
                self.v1 = argarray[1]
                
		return

        def execute(self):
                
                self.lib.lib_mav(self.v0,self.v1)
                
		return

        def toCommands(self):
                out = ""
		
		out+="mav("+str(self.v0)+","+str(self.v1)+");\n"
		
		return out

class slp_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
                self.v0 = argarray[0]
                
		return

        def execute(self):
                
                self.lib.lib_msleep(self.v0)
                
		return

        def toCommands(self):
                out = ""
		
		out+="msleep("+str(self.v0)+");\n"
		
		return out

class frz_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
                self.v0 = argarray[0]
                
		return

        def execute(self):
                
                self.lib.lib_freeze(self.v0)
                
		return

        def toCommands(self):
                out = ""
		
		out+="freeze("+str(self.v0)+");\n"
		
		return out

class mmr_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
                self.v0 = argarray[0]
                
                self.v1 = argarray[1]
                
                self.v2 = argarray[2]
                
                self.v3 = argarray[3]
                
		return

        def execute(self):
                
                self.lib.lib_motor(self.v0,self.v1)
                
                self.lib.lib_motor(self.v2,self.v3)
                
		return

        def toCommands(self):
                out = ""
		
		out+="motor("+str(self.v0)+","+str(self.v1)+");\n"
		
		out+="motor("+str(self.v2)+","+str(self.v3)+");\n"
		
		return out

class mmv_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
                self.v0 = argarray[0]
                
                self.v1 = argarray[1]
                
                self.v2 = argarray[2]
                
                self.v3 = argarray[3]
                
		return

        def execute(self):
                
                self.lib.lib_mav(self.v0,self.v1)
                
                self.lib.lib_mav(self.v2,self.v3)
                
		return

        def toCommands(self):
                out = ""
		
		out+="mav("+str(self.v0)+","+str(self.v1)+");\n"
		
		out+="mav("+str(self.v2)+","+str(self.v3)+");\n"
		
		return out

class amr_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
                self.v0 = argarray[0]
                
                self.v1 = argarray[1]
                
                self.v2 = argarray[2]
                
                self.v3 = argarray[3]
                
		return

        def execute(self):
                
                self.lib.lib_motor(0,self.v0)
                
                self.lib.lib_motor(1,self.v1)
                
                self.lib.lib_motor(2,self.v2)
                
                self.lib.lib_motor(3,self.v3)
                
		return

        def toCommands(self):
                out = ""
		
		out+="motor(0,"+str(self.v0)+");\n"
		
		out+="motor(1,"+str(self.v1)+");\n"
		
		out+="motor(2,"+str(self.v2)+");\n"
		
		out+="motor(3,"+str(self.v3)+");\n"
		
		return out

class amv_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
                self.v0 = argarray[0]
                
                self.v1 = argarray[1]
                
                self.v2 = argarray[2]
                
                self.v3 = argarray[3]
                
		return

        def execute(self):
                
                self.lib.lib_mav(0,self.v0)
                
                self.lib.lib_mav(1,self.v1)
                
                self.lib.lib_mav(2,self.v2)
                
                self.lib.lib_mav(3,self.v3)
                
		return

        def toCommands(self):
                out = ""
		
		out+="mav(0,"+str(self.v0)+");\n"
		
		out+="mav(1,"+str(self.v1)+");\n"
		
		out+="mav(2,"+str(self.v2)+");\n"
		
		out+="mav(3,"+str(self.v3)+");\n"
		
		return out

class mfz_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
                self.v0 = argarray[0]
                
                self.v1 = argarray[1]
                
		return

        def execute(self):
                
                self.lib.lib_freeze(self.v0)
                
                self.lib.lib_freeze(self.v1)
                
		return

        def toCommands(self):
                out = ""
		
		out+="freeze("+str(self.v0)+");\n"
		
		out+="freeze("+str(self.v1)+");\n"
		
		return out

class ssp_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
                self.v0 = argarray[0]
                
                self.v1 = argarray[1]
                
		return

        def execute(self):
                
                self.lib.lib_set_servo_position(self.v0,self.v1)
                
		return

        def toCommands(self):
                out = ""
		
		out+="set_servo_position("+str(self.v0)+","+str(self.v1)+");\n"
		
		return out

class ccn_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
		return

        def execute(self):
                
                self.lib.lib_create_connect()
                
		return

        def toCommands(self):
                out = ""
		
		out+="create_connect();\n"
		
		return out

class cdn_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
		return

        def execute(self):
                
                self.lib.lib_create_disconnect()
                
		return

        def toCommands(self):
                out = ""
		
		out+="create_disconnect();\n"
		
		return out

class cdd_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
                self.v0 = argarray[0]
                
                self.v1 = argarray[1]
                
		return

        def execute(self):
                
                self.lib.lib_create_drive_direct(self.v0,self.v1)
                
		return

        def toCommands(self):
                out = ""
		
		out+="create_drive_direct("+str(self.v0)+","+str(self.v1)+");\n"
		
		return out

class esv_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
		return

        def execute(self):
                
                self.lib.lib_enable_servos()
                
		return

        def toCommands(self):
                out = ""
		
		out+="enable_servos();\n"
		
		return out

class ao_Command(Command):
        def create_from(self, argarray, execLib):
		self.lib = execLib
                
		return

        def execute(self):
                
                self.lib.lib_ao()
                
		return

        def toCommands(self):
                out = ""
		
		out+="ao();\n"
		
		return out



commandSet = dict(

 mtr=mtr_Command ,

 mav=mav_Command ,

 slp=slp_Command ,

 frz=frz_Command ,

 mmr=mmr_Command ,

 mmv=mmv_Command ,

 amr=amr_Command ,

 amv=amv_Command ,

 mfz=mfz_Command ,

 ssp=ssp_Command ,

 ccn=ccn_Command ,

 cdn=cdn_Command ,

 cdd=cdd_Command ,

 esv=esv_Command ,

 ao=ao_Command 

)