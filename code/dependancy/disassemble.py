import os
def disassemble(directory,filename,file):
	if(os.path.exists(directory)):
		print "Decoding ", filename
		print directory
		
		choice  = raw_input("Do you want to replace existing directory?(yes/no)")
		if choice == 'yes':
			apk = 'apktool d '+ filename +' -f'
			os.system(apk)
		else:
			exit()
	else:
		apk = 'apktool d '+ filename 
		os.system(apk)
	mv = 'mv '+os.getcwd()+'/'+file+' '+os.getcwd()+'/Data/Apk_data/'+file+'/'+file
	os.system(mv) 
