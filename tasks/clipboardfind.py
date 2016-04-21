import pyperclip

__command__ = "findc"
__usage__ = "findc"
__description__ = "Search in clipboard content"

def run(shell, args): 		
	print("searching for "+args[0])
	content = pyperclip.paste()
	result = ""
	if content is None or len(content) == 0 :
		return result
	for line in content.splitlines() :
		if args[0].lower() in line.lower() : 
			result = result + line + "\r\n"
			return result