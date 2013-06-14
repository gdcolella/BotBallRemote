import json, re
from jinja2 import Environment, Template, FileSystemLoader

SRCDIR = '../src/'
DSTDIR = '../bin/'

OUTFILE = 'ControlLibrary.c'
DBGFILE = 'DebugLibrary.c'

environment = Environment(loader = FileSystemLoader(SRCDIR))

libraryTemplate = environment.get_template("LibraryTemplate")
debugTemplate = environment.get_template("DebugTemplate")

with open(SRCDIR + 'Command.json') as data_file:
	data = json.load(data_file)

for i in range(len(data["commands"])) :
	data["commands"][i]["numargs"] = int(data["commands"][i]["numargs"])

writeStr = ""
debugStr = ""

writeStr += libraryTemplate.render(commands = data["commands"])
debugStr += debugTemplate.render(commands = data["commands"])

with open(DSTDIR + OUTFILE, 'w') as outfile:
	outfile.write(writeStr)
with open(DSTDIR + DBGFILE, 'w') as outfile:
	outfile.write(debugStr)
