from shortcuts import *

__command__ = "alias"
__usage__ = "alias"
__description__ = "View shortcuts"

def run(shell, args): 
	result = ""
	if len(args) == 0 :
		for var in alias(): 
			print(var + " = " + str(alias_value(var)))
	else :
		result = str(alias_value(args[0]))
	return result
		
	