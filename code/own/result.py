import os,sys

def printResult(directory,declared_permission_count,pp):
	base=os.path.basename(directory)
	permission_file = os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'permission.txt'
	required_permission_count = len(pp)
	permission_f = open(permission_file,'r')
	data=permission_f.readlines()
	permission_used=0
	user_permission=0
	for permission in data:
		if permission.replace('\n','') in pp:
			permission_used=permission_used+1
		else:
			word = permission.replace('\n','').split('.')
			if word[0] == 'com':
				user_permission = user_permission + 1
	permission_not_declared = len(pp)-permission_used
	unnecessary_declaration = declared_permission_count-permission_used-user_permission
	print "***Permission Statistics in Numeric Form***"
	print "Permissions declared",declared_permission_count
	print "Permissions required",len(pp)
	print "Permissions used from declaration",permission_used
	print "Unecessary declaration",unnecessary_declaration
	print "Permissions required but not declared",permission_not_declared
