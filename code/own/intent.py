import os,sys

def checkintent(directory,pp):
	base=os.path.basename(directory)
	in_path= os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'method.json'			# input file path.
	out_path = os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'intentpermission.txt'
	no='22'
	intent_path = os.getcwd()+'/Data/Pscout_input_api'+no+'/intentpermission'
	print "Checking for intent permissions.."
	orig_stdout = sys.stdout                                                # To write output to txt file using stdout.
	f = file(out_path, 'w')						# creating file object ....
	sys.stdout = f
	searchfile = open(intent_path, "r")
	for line in searchfile:
		str = line.split(' ') 
		data = open(in_path, "r")
		for line1 in data:
			if str[0] in line1:
				print str[0] + " found at " + line1.replace(' ','').replace('\n','') + " for permission " + str[1]
				if str[1] not in pp:
					pp.add(str[1])
			     	
	searchfile.close()
	data.close()
	sys.stdout = orig_stdout						# To write output to txt file using stdout.
	#f.close() 								# close file.
	print out_path," created"
	return pp
