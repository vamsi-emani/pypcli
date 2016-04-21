import pyperclip
import json 

__command__ = "ppj"
__usage__ = "ppj"
__description__ = "Pretty print json"

def run(shell, args):	
	if len(args) == 0 :
		jsonBody = shell.multilineInput()	 
		print(jsonBody)
		try : 
			parsed = json.loads(jsonBody)
			return json.dumps(parsed, indent=2, sort_keys=True)	
		except Exception as e : 			
			raise shell.error(e, "Not a valid json ")
	else:
		return ""


