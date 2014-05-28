'''
Created on 07/03/2012

@author: lucask
'''

from files.fileHandle import *
from loggingCustom.LoggerCustom import *
from propertiesFolder.propertiesCustom import *

import re
import logging.config
import logging
    
#####################################################################################################
#
#
#
#####################################################################################################

if __name__ == '__main__':

    logging.config.fileConfig('../loggingCustom/logging.conf')

    # create logger
    logger = logging.getLogger('simpleExample2')

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
    
    print getProperties('htmlHandle', 'host')
    
#    urlRoot = "http://zbor.openet-telecom.lan/~tester3/newreport/"
#    url = urlRoot+"/PHONE.PHONE-AC.PHONE-AC-018//PHONE_PHONE_AC_018.act/"+\
#                    "/RunDsdUnitTests_test.dsdu_PMATF_6000000/7table5.html"
#    url = "http://zbor.openet-telecom.lan/~tester3/newreport//PHONE.PHONE-AC.PHONE-AC-002//PHONE_PHONE_AC_002.act//RunDsdUnitTests_test.dsdu_PMATF_6000000//14table3.html"
#    findStringUrl(url,'GX_RAR_INITIAL')
#    cmd = 'C:"\Program Files (x86)"\WinMerge\WinMergeU.exe expected.txt actual.txt'
#    runCommand(cmd)
#    removeLine("CiscoGxR6.0v10-Event-Trigger PLMN_CHANGE RAT_CHANGE QOS_CHANGE MULTI")
#    
#    rootdir = 'C:\\eclipse\\workspace\\cpm30\\acceptance.ciscoR6\\LTE\\POL-COMMON'
#    removeTempFiles()
    
#    phone = "2004-959-559 #This is Phone Number"
#    print re.sub(r'#.*$', "", phone)
    
    
#    rootdir = 'C:\\eclipse\\workspace\\cpm31\\acceptance.ciscoR6\\PHONE\\POL-CORE'
#    filename = "inputAvs.cfg"
#    fileList = findFiles(filename,rootdir)
#    for files in fileList:
#        replaceLine("RAT_CHANGE QOS_CHANGE", files, "")
#        
#    removeTempFiles()
#        os.rename(files, files+".tmp")
#        fin = open(files+".tmp")
#        fout = open(files, 'w')
#        strin = fin.read()
#        #pattern = re.compile('AVS::Dia-Attr-CiscoGxR6.0v10-Service-Status MULTI\n*7-A-ACT\n*\n*\nEND AVS')
#        strin = re.sub(r'AVS::Dia-Attr-CiscoGxR6.0v10-Service-Status MULTI*\n*7-A-ACT*\n*\n*\n*END AVS',"",strin)
#        #strin = strin.replace(str,newstr)
#        #fout.write(strin)
#        fin.close()
#        fout.close()
#    removing tmp file
#    removeGroupLines("AVS::Dia-Attr-CiscoGxR6.0v10-Service-Status MULTI\n*7-A-ACT\n*\n*\nEND AVS", files, "")
#            
#        print re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',r'static PyObject*\npy_\1(void)\n{','def myfunc():')
#    print 'teste'
