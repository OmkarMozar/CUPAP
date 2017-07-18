import os,sys


def checkcontentprovider(directory,pp):
	base=os.path.basename(directory)
	in_path= os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'method.json'			# input file path.
	out_path = os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'contentpermission.txt'
	no='22'
	content_path = os.getcwd()+'/Data/Pscout_input_api'+no+'/contentproviderpermission'
	print "Checking for content permissions.."
	orig_stdout = sys.stdout                                                # To write output to txt file using stdout.
	f = file(out_path, 'w')						# creating file object ....
	sys.stdout = f

	searchfile = open(content_path, "r")
	for line in searchfile:
		str = line.split(' ') 
		data = open(in_path, "r")
		for line1 in data:
			if str[0] in line1:
				if str[1]=='R' or str1[1]=='W':
					print str[0] + "found at " + line1.replace(' ','').replace('\n','') + "for permission " + str[2].replace('\n','')
					if str[2] not in pp:
						pp.add(str[2].replace('\n',''))

		     		else:
					print str[0] + "found at " + line1.replace(' ','').replace('\n','') + "for permission " + str[1].replace('\n','')
					if str[1] not in pp:
						pp.add(str[1].replace('\n',''))

	
	searchfile.close()
	data.close()
	sys.stdout = orig_stdout						# To write output to txt file using stdout.
	#f.close() 								# close file.
	print out_path," created"
	for i in pp:
		print i
	return pp
