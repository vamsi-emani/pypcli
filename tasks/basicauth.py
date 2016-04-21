import urllib
import urllib.request

__command__ = "basicauth"
__usage__ = "basicauth"
__description__ = "Basic authentication"

def run(shell, args): 		
	SERVER = args[0]
	authinfo = urllib.request.HTTPPasswordMgrWithDefaultRealm()
	username = args[1]
	password = args[2]
	authinfo.add_password(None, SERVER, username, password)
	page = 'HTTP://'+SERVER+'/cgi-bin/tools/orders_waiting.py'
	handler = urllib.request.HTTPBasicAuthHandler(authinfo)
	myopener = urllib.request.build_opener(handler)
	opened = urllib.request.install_opener(myopener)
	output = urllib.request.urlopen(page)
	do_something(output)

