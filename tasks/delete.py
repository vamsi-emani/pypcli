import os
import shutil
from shortcuts import *

__command__ = "rm"
__usage__ = "rm"
__description__ = "Delete files and folders"

def delete(path):
	try :
		if os.path.isfile(path) :
			os.remove(path)
		else :
			shutil.rmtree(path)
	except Exception as e: 
		print("Error deleting "+path+" : "+str(e))

def run(shell, args): 
	if len(args) == 0 :			
		os.system("del "+plogs+"*.*")			
	else :		
		for item in args:			
			delete(item)
	return ""	
