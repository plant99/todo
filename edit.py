import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
def edit_handler(serial):
	newTask = raw_input("Enter task details: ")
	priority = raw_input("Priority: ")
	f = open(dir_path+'/todo.txt', 'r')
	previousContent = f.read()
	f.close()
	previousContent = previousContent.split('\n')
	previousContent[serial] = newTask+'-'+priority
	previousContent = '\n'.join(previousContent)
	f = open('/home/shivashis/Documents/lifeLine/projPer/todo/todo.txt', 'w')
	f.write(previousContent)
	f.close()