
import os 

__command__ = "nof"
__usage__ = "nof folder-path ext-mask"
__description__ = "Count no. of files in folder"

def run(shell, args): 	
	path = "" if len(args) == 0 else args[0]
	mask = "" if not len(args) == 2 else args[1]
	if os.path.isfile(path) : 
		print("expected folder path got file path")
		return 0
	else :
		num_files = 0
		for root, dirnames, filenames in os.walk(path):
			for filename in filenames:
				if len(mask) == 0 or filename.endswith(mask) :								
					num_files = num_files + 1
		return "Total number of " +mask+" files in directory " +path+" : "+str(num_files)
	