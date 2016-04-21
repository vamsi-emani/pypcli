# pypcli
Python Pluggable Command Line Interface

Developers come across many minor mundane and repetitive tasks while development. 
Many a time we may query on google for "Base 64 url endoder online" or "pretty print json online".
Or one might want to search for a file or some keyword in a huge source code base. 
Developers who lack patience to repetitively spend time on such mundane taks tend to 
write utility programs that can get around these tasks easily. 

Pypcli is a command line interface that can map tasks or utility programs to a 
shell command. It has basic shell features like the ability to take 
multiliine inputs, ability to remember last command, etc. 
Users can write their own tasks (shell commands) and execute them from pypcli 
simply by providing the mapped command and arguments, if any.


### How to run
 
 Install python and from command line execute
 python pypcli.py
 
### How to write a pluggable shell task

Writing your own pluggable shell task is very easy. Just create .py file that adheres to the below format
and place the .py file in "tasks" directory. When done so, the task automatically gets plugged into the shell.
For instance, to create a utility that can base64 encode a given input, Create some file urlb64encode.py

```
import base64

__command__ = "urlenc"
__usage__ = "urlenc {arg}"
__description__ = "Base64 URL Safe Encode"


def run(shell, args): 
	if len(args) == 0 :
		return "Please specify input to encode."
	else :			
		return str(base64.urlsafe_b64encode(bytes(args[0], encoding='utf-8'))).split("'")[1].strip()	
```
	
It is essential to provide `__command__`,`__usage__` and `__description__` variables for the runnable utility task along with
implementation for the `run()` method. Once placed into the tasks directory. When you restart pypcli the task is plugged into the
shell and can be run straight away with the mapped command specified in the runnable task.

```
Shell>> urlenc https://www.google.com

aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbQ==
```

The idea is to extend this by provding as many implementations as possible for various repetitive development tasks
so that a developer can carry this shell and make the best out of it during all development projects. 








