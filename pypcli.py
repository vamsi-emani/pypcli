import sys;
import os;	
import pyperclip;
import traceback;
import datetime
import utils
import time
from shortcuts import *

class ShellCommand : 

	def __init__(self, rawtext):
		self.rawtext = rawtext
		self.result = ""
		tokens = rawtext.split(' ');
		command = tokens[0]
		if command in alias() : 
			self.cmd = alias_value(command)
			self.is_command_refined = True
		else :
			self.cmd = command
			self.is_command_refined = False

		args = tokens[1:] if len(tokens) > 1 else []		
		self.args = []
		self.is_arguments_refined = False
		for arg in args :
			if arg in alias() :
				self.args.append(alias_value(arg))	
				self.is_arguments_refined = True
			else :
				self.args.append(arg)				

	def getCommand(self):
		return self.cmd + " "+ " ".join(self.args)

	def asString(self):		 
		return (self.cmd, self.args)

	def isQuit(self):
		return self.cmd == "quit"

	def isLast(self): 
		return self.cmd == "last"

	def isHelp(self):
		return self.cmd == "help"

	def hasResult(self) : 
		return self.result is not None and len(str(self.result)) is not None

class ShellTaskError(Exception) :	
	def __init__(self, error, msg) : 
		self.error = error
		self.msg = msg
		
class Shell :

	COL_1_WIDTH = 35
	COL_2_WIDTH = 24						

	def __init__(self):
		"""self.getch = utils._Getch()			
		self.putch = utils._Putch()"""
		self.tasks = {}	
		self.verbose = False	
		self.last = ShellCommand("help")
		for task in os.listdir("tasks"):
			if task.endswith(".py") :				
				file_without_extn = task[:-3]
				invocable_shell_task = self.registerTask(file_without_extn)
				if invocable_shell_task is not None : 									
					self.tasks[invocable_shell_task.__command__] = invocable_shell_task

	def setVerbose(self) :
		self.verbose = True			

	def startUpInfo(self):
		self.logDebug("Verbose mode : "+str(self.verbose))
		self.logDebug("Tasks found : "+str(len(self.tasks)))		
		for task in self.tasks : 
			self.logDebug("Registered shell task : " + task)

	def welcome(self): 
		print("")
		print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")		
		print("*                                                           *")
		print("*             ____  __  __  ___  __    __                   *")
		print("*            / __/ / /_/ / /_ / / /   / /                   *")
		print("*           _\ \  / __  / /_/  / /__ / /__                  *")
		print("*          /___/ /_/ /_/ /___//____//____/                  *")
		print("*                                                           *")
		print("*             Version : 1.0                                 *")
		print("*             Author  : Vamsi Emani                         *")
		print("*                                                           *")
		print("*                                                           *")
		print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")		
		print("")

	def help(self):	
		print(self.lineSeparator())	
		print(self.row('COMMAND DESCRIPTION', 'USAGE'))
		print(self.lineSeparator())	
		for cmd, task in sorted(self.tasks.items()) :
			if len(task.__description__) > 35 or len(task.__usage__) > 20 :
				print(self.multiRow(task))
			else :
				print(self.row(task.__description__, task.__usage__))		
		print(self.row('Quit the shell', 'quit'))						
		print(self.lineSeparator())	
	
	def multiRow(self, task):
		line = task.__description__ 
		multirow = ''
		COL1WD = Shell.COL_1_WIDTH		
		descriptions = [line[i:i+COL1WD] for i in range(0, len(line), COL1WD)]
		i = 0
		for description in descriptions :
			if i == 0 :
				multirow = multirow + self.row(description, task.__usage__)+"\n"
			else :
				multirow = multirow + self.row(description, "")+"\n"
			i = i + 1;
		return multirow.strip()


	def row(self, col1, col2):
		return "| "+col1.ljust(Shell.COL_1_WIDTH)+"| "+col2.ljust(Shell.COL_2_WIDTH)+"|"
				

	def multilineInput(self) :
		prefix = "  |  "
		print("Shell>> You have entered multi-line input mode. Type your text and press ! to exit multi-line input mode.")
		str = ""	
		while (not str.endswith("!")) :			
			str = str + input(prefix)
		return str[:-1]

	def getLine(self, identifier) :
		print(identifier, end='')		
		txt = ''
		while not txt.endswith('\r') or txt.endswith('\n') :
			bytestring = self.getch()
			char = bytestring.decode("utf-8")			
			txt = txt + char			
		return txt.strip()			

	def interact(self):		
		txt = input("Shell>> ")										
		while (txt.strip() != "quit") :
			self.execute(txt)
			txt = input("Shell>> ")
		
	def execute(self, text) :
		try :
			shellCommand = ShellCommand(text)
			self._execute(shellCommand)
		except Exception as e:
			print("Shell task error while executing "+shellCommand.cmd + " : "+ str(e))
			if(self.verbose) :
				traceback.print_exc()
			
	def registerTask(self, module):
		try :				
			return getattr(__import__("tasks."+module, globals=globals()), module)	
		except Exception as e:
			logDebug("Unable to register shell task "+module)

	def logDebug(self, msg):
		if(self.verbose == True) :
			print("Debug : "+str(msg))

	def error(self, error, msg) : 
		return ShellTaskError(error, msg)
		
	def _execute(self, shellCommand):				
		task = self.tasks.get(shellCommand.cmd)						
		self.logDebug("Invoking : "+str(shellCommand.asString()))
		if shellCommand.isQuit() : 
			sys.exit()
		elif shellCommand.isHelp() :
			self.help()
		elif shellCommand.isLast():
			self.previousOutput()			
		elif task is None :			
			os.system(shellCommand.getCommand())
		else :
			shellCommand.result = task.run(self, shellCommand.args)				
		self.displayResult(shellCommand.result)	
		if not shellCommand.isLast() :
			self.last = shellCommand
		return shellCommand.result			
		
	def displayResult(self, result):
		if result is None :
			return
		print("")
		if type(result) is list :
			for item in result:
				print(item)
		else :
			print(result)	

	def lineSeparator(self):
		return "+------------------------------------+-------------------------+"

	def previousOutput(self):
		self.displayResult(self.last.result)
		"""if self.last.result is not None :
			cmd = self.last[0] if type(self.last) is list else str(self.last)
			os.system('"'+cmd+'"'	)"""

def main(args) :						
	shell = Shell()
	if "-v" in args : 
		shell.setVerbose()
	shell.welcome()
	shell.startUpInfo()
	shell.execute("help")
	shell.interact()					
		

		
if __name__ == '__main__':														
	main(sys.argv)