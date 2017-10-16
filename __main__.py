import argparse
import sys
import add
import delete
import edit
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
parser = argparse.ArgumentParser(description='Simple todo CLI')
parser.add_argument('-en','--enable', help="Enable the todo", action="store_true")
parser.add_argument('-db','--disable', help="Disable the todo", action="store_true")
parser.add_argument('-n','--newtask', help="Add new task")
parser.add_argument('-d','--delete', type=int,help="Delete a task")
parser.add_argument('-e','--edit', type=int,help="Edit a task")
args = parser.parse_args()


def modify(flag):
	f = open(dir_path+'/todo.txt', 'r')
	previousContent = f.read()
	f.close()
	previousContent = previousContent.split('\n')
	previousContent[0] = flag
	previousContent = '\n'.join(previousContent)
	f = open(dir_path+'/todo.txt', 'w')
	f.write(previousContent)
	f.close()

if args.enable and args.disable:
	print "Pass any one flag!"
	sys.exit()

if args.enable:
	modify('e')
	sys.exit()

if args.disable:
	modify('d')
	sys.exit()

if args.newtask:
	priority = raw_input("Priority on a scale of 1-3?")
	add.add_handler(args.newtask, priority)
	sys.exit()

if args.delete:
	delete.delete_handler(args.delete)
	sys.exit()

if args.edit:
	edit.edit_handler(args.edit)
	sys.exit()

"""
WAS USED TO say status-(e/d)
previousContent[0] = previousContent[0].split('-')
	previousContent[0][1] = 'd'
"""

f = open(dir_path+'/todo.txt', 'r')
content = f.read().split('\n')
count = len(content)
i = 1
while i<= count-1:
	line = content[i].split('-')
	priority = int(line.pop())
	line = '-'.join(line)
	print  "\033[1;36;40m"+'*'*priority +"\033[0m"+str(i)+') '+ line
	i+=1

f.close()
"""content = f.read().split('\n')
for line in content:
	print line
	"""