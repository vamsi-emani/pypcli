import glob
import os
from pathlib import Path


__command__ = "search"
__usage__ = "search {path}"
__description__ = "Search filenames in directory"

def run(shell, args):
	dir_count = 0
	file_count = 0 
	rootDir = '.' if len(args) == 0 else args[0]
	filename = "" if len(args) < 2 else args[1]
	result = []
	print("-> searching files and directories for "+filename)
	for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
		if(filename in dirName) :
			print(dirName)
		dir_count = dir_count + 1
		for fname in fileList:
			if(filename in fname) :
				fullpath = dirName+"\\"+fname
				result.append(fullpath)
				print(fname + "  ["+fullpath+"]")
			file_count = file_count + 1
	print("-------------------------------------")
	print("Traversed Directory : " + rootDir)
	print("Directory count     : " + str(dir_count))
	print("File count          : " + str(file_count))
	print("-------------------------------------")
	return result