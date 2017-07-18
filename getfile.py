import code.own.getfile as getfile
import code.dependancy.disassemble as dis
import code.own.manifestparser as mp
import code.dependancy.smaliparser as sp
import code.own.jsonparser as jp
import code.own.edit as edit
import code.own.duplicateMethodRemover as rd
import code.own.bmapping as bm
import code.own.intent as ip
import code.own.contentprovider as cp 
import code.own.result as result
import os
apk = getfile.getFile(os.getcwd()) #apk file
apkf = os.path.basename(apk)
directory = os.getcwd() + "/Data/Apk_data/" + apkf.replace('.apk','')+"/" +apkf.replace('.apk','')
#print os.getcwd()
print apk
print apkf
print directory
print  os.getcwd()
pp = set()
file = apkf.replace('.apk','')
#dis.disassemble(directory,apk,file)
#declared_permission_count = mp.parsexml(directory)
#sp.parsesmali(directory)
#jp.parsejson(directory)
#edit.editstyle(directory)
#rd.removered(directory)
pp = bm.binarymapping(directory)
pp = ip.checkintent(directory,pp)
pp = cp.checkcontentprovider(directory,pp)
#result.printResult(directory,declared_permission_count,pp)
result.printResult(directory,38,pp)
