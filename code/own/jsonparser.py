import json
import os
import sys

def parsejson(directory):
	
	base=os.path.basename(directory)	
	in_path= os.getcwd()+'/Data/Apk_data/'+base+'/'+base+"method.json"			# input file path.
	out_path = os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'method.csv'	
#	out_path= os.path.join(directoryoutfile)					# output file path.
	print "Parsing json file.."

	orig_stdout = sys.stdout                                                # To write output to txt file using stdout.
	f = file(out_path, 'w')						# creating file object ....
	sys.stdout = f							
	with open(in_path) as jsonData:
		data = json.load(jsonData)
		classes = data['classes']
		for element in classes:
			methods = classes[element]['methods']	
			for name in methods:
				#print '"',element,'"| ',name['return'],'"| "',name['name'],'"| "',name['args'],'"'
				#print name['name']
	 			print  '"',element,'"| "', name['return'],'"| "', name['name'],'"| "', name['args'],'"'
				calls = name['calls']
				for call in calls:
					print  '"',call['to_class'],'"| "', call['return'],'"| "', call['to_method'],'"| "', call['local_args'],'"'

	sys.stdout = orig_stdout						# To write output to txt file using stdout.
	f.close() 								# close file.
	print out_path," created"
	

