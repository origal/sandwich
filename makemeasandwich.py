#!/usr/bin/python
# Y U lookin' at mah code?!

import subprocess
def make():
	p = subprocess.Popen("whoami", stdout=subprocess.PIPE)
	userName = p.communicate()[0]
	if (userName[:4] == "root" and not userName[4:].isalpha()):
	 	print("Ok, done.")
	 	return
	else:
		print("no way, who are you to tell me what to do?")
if __name__ == "__main__": make()
