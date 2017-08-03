import subprocess
import time

def play(filename):
	name = 'afplay ' + filename
	proc = subprocess.Popen([name], shell = True)
	return proc #SAVE THIS so you can terminate it

def stop(proc):
	proc.terminate()
	return 0