import os
import sys
import fileinput

def editstyle(directory):
	# Read in the file
	filedata = None
	base=os.path.basename(directory)	
	out_path = os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'method.csv'	
	with open(out_path, 'r') as file :
	  filedata = file.read()

	# Replace the target string
	filedata = filedata.replace('{', '')
	filedata = filedata.replace('}', '')
	filedata = filedata.replace(', ', ';')
	filedata = filedata.replace('| ', ',')
	filedata = filedata.replace(' ', '')
	# Write the file out again
	with open(out_path, 'w') as file:
	  file.write(filedata)

	file.close()
	print out_path," edited"
