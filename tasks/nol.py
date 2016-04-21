
import os 

__command__ = "nol"
__usage__ = "nol folder-path ext-mask"
__description__ = "Count no. of lines in file or folder path"

def count_lines(file):
	num_lines = 0
	try : 
		num_lines = sum(1 for line in open(file))
		print(file + ":" + str(num_lines))
	except : 
		print("error counting lines in "+file)
	return num_lines

def run(shell, args): 	
	path = "" if len(args) == 0 else args[0]
	mask = "" if not len(args) == 2 else args[1]
	if os.path.isfile(path) : 
		print("file")
		return count_lines(path)
	else :
		num_lines = 0
		for root, dirnames, filenames in os.walk(path):
			for filename in filenames:
				if len(mask) == 0 or filename.endswith(mask) :
					file_lines = count_lines(os.path.join(root, filename))				
					num_lines = num_lines + file_lines
		return "Total " + mask + " file lines in directory " +path+" : "+str(num_lines)
	