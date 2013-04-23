import json, re
from jinja2 import Environment, Template, FileSystemLoader

SRCDIR = '../src/'
DSTDIR = '../upload/'

OUTFILE = 'Commands_gen.py'

#for this purpose, use
# search = 'v[0-9]'
# replace= "+str(\g<0>)+"
def re_sub(instr, search, replace):
	return re.sub(search,replace,instr)

environment = Environment(loader=FileSystemLoader(SRCDIR) )

environment.filters['re_sub'] = re_sub

commandTemplate = environment.get_template("CommandTemplate")


#print commandTemplate.render(prefix = 'mav', numargs = 5, functions = ["mav(v0,v1)"])

with open(SRCDIR + 'Command.json') as data_file:
	data = json.load(data_file)
for i in range( len( data["commands"] ) ):
	data["commands"][i]["numargs"] = int(data["commands"][i]["numargs"])


writeStr = ""

writeStr += commandTemplate.render(commands = data["commands"])

with open(DSTDIR + OUTFILE, 'w') as outfile:
	outfile.write(writeStr)


