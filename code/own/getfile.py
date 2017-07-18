import os

def getFile(cwd):
	filename = raw_input("Enter a file name:")
	if(os.path.exists(filename)):
			apk = os.path.basename(filename)
			apkf = apk.replace('.apk','')
			mkdir = 'mkdir '+cwd+'/Data/Apk_data/'+apkf
			#print mkdir
			os.system(mkdir)
			if(os.path.abspath(filename)):
				copy = 'cp ' + filename +' '+ cwd+'/Data/Apk_data/'+apkf+'/'+apk
				os.system(copy)
			#	print copy
				return cwd+'/Data/Apk_data/'+apkf+'/'+apk
			else:
				copy = 'cp ' + filename +' '+ cwd+'/Data/Apk_data/'+apkf+'/'+apk
				os.system(copy)
				return os.path(filename)
	else:
			print "No such file exists"
			exit()
