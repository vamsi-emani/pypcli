import base64

__command__ = "urlenc"
__usage__ = "urlenc {arg}"
__description__ = "Base64 URL Safe Encode"


def run(shell, args): 
	if len(args) == 0 :
		return "Url needed as argument"
	else :			
		return str(base64.urlsafe_b64encode(bytes(args[0], encoding='utf-8'))).split("'")[1].strip()	