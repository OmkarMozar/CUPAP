import os,sys

def binarymapping(directory):
	
	base=os.path.basename(directory)
	in_path= os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'method.csv'			# input file path.
	out_path = os.getcwd()+'/Data/Apk_data/'+base+'/'+base+'mapping.txt'
	no='22'
	pscout_path = os.getcwd()+'/Data/Pscout_input_api'+no+'/pscout-mapping.csv'
	print "Mapping.."
	orig_stdout = sys.stdout                                                # To write output to txt file using stdout.
	f = file(out_path, 'w')						# creating file object ....
	sys.stdout = f

	pf = open(pscout_path,'r')
	x=pf.readlines()
	pf.close()
	vik=[]
	for i in range(0,len(x)):
		vik.append(x[i].split(','))
	v= sorted(vik,key=lambda l:l[3], reverse=False)
	v=zip(*v)
	pf1=open(in_path,'r')
	f=pf1.readlines()
	pf1.close()
	g=[]
	for i in range(0,len(f)):
		g.append(f[i].split(','))
	alist=g
	pp = set()	
	count=0
	for i in range(0,len(alist)):
		alist[i][0] =alist[i][0].replace('"','')
		alist[i][0]=' "'+alist[i][0]+';"'
		alist[i][1]=alist[i][1].replace('"','"')
		alist[i][2]=alist[i][2].replace('"','"')
		alist[i][3]=alist[i][3].replace('"','"')
		bss(alist[i][0],alist[i][1],alist[i][2],v,pp)
	#print count
	#print len(pp)
	#for i in pp:
	#	print i
	pf1.close()
	sys.stdout = orig_stdout						# To write output to txt file using stdout.
	#f.close() 
	print out_path," created"
	return pp
def bss(a,b,c,s,pp):
	seq=s[3]
	a1=s[1]
	b1=s[2]
	min = 0
	max = len(seq) - 1
	count=0
	flag=0
	while min<max:
		m = (min + max) // 2
        	if seq[m] < c:
           		min = m + 1
        	elif seq[m] > c:
        		max = m - 1
        	else:		
			x=m-1
			while a1[m]==a and b1[m]==b:
				print s[0][m],',',s[3][m],',',s[2][m],',',s[1][m]
				if s[0][m] not in pp:
					pp.add(s[0][m].replace('"',''))
				flag=1
				m=m+1
			while a1[x]==a and b1[x]==b:
				print s[0][m],',',s[3][m],',',s[2][m],',',s[1][m]
				if s[0][m] not in pp:
					pp.add(s[0][m].replace('"',''))
				flag=1
				x=x-1

			break
	if flag==1:
		return 1
	else:
		return 0

	
			
	
	


