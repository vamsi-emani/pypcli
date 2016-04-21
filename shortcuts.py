phtml = 'D:\\autodesk\\Pserver6.0\\server\\nodes\\default\\archives\\public_html\\'
plogs = 'D:\\autodesk\\Pserver6.0\\server\\nodes\\default\\logs\\'
music = "C:\\Program Files (x86)\\foobar2000\\foobar2000.exe"
mrepo = 'D:\\vamsi\\music\\'

def alias_value(key):
	return globals()[key]

def alias():
	exclude = ['alias_value', '__builtins__', '__name__', '__spec__', '__loader__', '__doc__', '__file__', 'alias', '__package__', '__cached__']	
	return list(set(globals()) - set(exclude))
	