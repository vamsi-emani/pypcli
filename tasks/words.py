
__command__ = "strlen"
__usage__ = "strlen"
__description__ = "Text length"

def run(shell, args): 	
	keyword = "" if len(args) == 0 else args[0]
	lines = shell.multilineInput()
	print("Number of characters with spaces : "+ str(len(lines)))
	print("Number of alphanumeric characters : "+  str(len( "".join(lines.split())  )))	
	return ""
		
	