#
# @author BE_PROJECT_05_omkar
#

import sys
from xml.dom import minidom
import os
def parsexml(directory):
#	di = directory.replace('.apk','')
	base=os.path.basename(directory)
	in_path= os.getcwd()+'/Data/Apk_data/'+base+'/'+base+"/AndroidManifest.xml"			# input file path.
		
	
	out_path = os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'permission.txt'	
#	out_path= os.path.join(directoryoutfile)					# output file path.
	print "Parsing AndroidManifest.xml.."

	orig_stdout = sys.stdout                                                # To write output to txt file using stdout.
	f = file(out_path, 'w')						# creating file object ....
	sys.stdout = f								# initialising file object.....
	
	count = 0

	xmldoc = minidom.parse(in_path)					# Xml parsing of manifest file  
	permission_tag=xmldoc.getElementsByTagName('uses-permission')           # to retrive permissions
										# requested by andriod application.

	for node in permission_tag:						
		permission=node.getAttribute('android:name')			# getting attribute name permission....
		print permission						# printing permissions...
		count = count+1
	#print count
	sys.stdout = orig_stdout						# To write output to txt file using stdout.
	f.close() 								# close file.
	print out_path," created"
	result_path = os.getcwd()+'/Data/Apk_data/'+base+'/result'
	filer = open(result_path,'w')
	filer.write('No of declared permission = '+str(count))
	filer.close()	
	return count


