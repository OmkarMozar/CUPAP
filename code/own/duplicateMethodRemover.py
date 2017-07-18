import os
def removered(directory):
	base=os.path.basename(directory)
	input_path = os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'method.csv'
	output_path = os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'methodu.csv'
	inputFile = open(input_path,'r')
	outputFile = open(output_path,'w')
	uniqueMethods = set() 
	for line in inputFile:
	    if line not in uniqueMethods:
		outputFile.write(line)
		uniqueMethods.add(line)
	outputFile.close()
	inputFile.close()
	#print outputFile," created"
	print "Redundant methods removed"
	os.remove(input_path)
	os.rename(output_path,input_path)
