import base64

__command__ = "urldec"
__usage__ = "urldec {arg}"
__description__ = "Base64 URL Safe Decode"


def run(shell, args): 
	if len(args) == 0 :
		return "Url needed as argument"
	else :
		target = args[0]
	return str(base64.urlsafe_b64decode(bytes(args[0], encoding='utf-8')));	