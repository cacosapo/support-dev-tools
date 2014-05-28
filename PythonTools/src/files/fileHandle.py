'''
Created on 14/03/2012

@author: lucask
'''

'''

    functions related to file handle
 
'''

import os
import sys
import re

#####################################################################################################
#
# Find an specific file in a folder
#
#####################################################################################################
def findFiles(str, rootdir):
    fileList = []
    for root, subFolders, files in os.walk(rootdir):
        for file in files:
            if re.search(str, file, re.IGNORECASE) != None:
                fileList.append(os.path.join(root, file))
    print fileList
    return fileList

#####################################################################################################
#
# Remove specific line from a file
#
#####################################################################################################

def removeLine(str, filename):
    #os.chdir('C:\\eclipse\\workspace\\cpm30\\acceptance.ciscoR6\\LTE\\POL-COMMON\\POL-COMMON-002')
    #create temp file
    os.rename(filename, filename + ".tmp")
    fin = open(filename + ".tmp")
    fout = open(filename, 'w')
    for line in fin.readlines():
        if re.search(str, line, re.IGNORECASE) == None:       
            fout.write(line)
    fin.close()
    fout.close()
    #removing tmp file
    #if os.path.exists(filename+".tmp"):
    #    os.remove(filename+".tmp")

#####################################################################################################
#
# Replace str fo new str into a file
#
#####################################################################################################
def replaceLine(str, filename, newstr):
    #os.chdir('C:\\eclipse\\workspace\\cpm30\\acceptance.ciscoR6\\LTE\\POL-COMMON\\POL-COMMON-002')
    #create temp file
    os.rename(filename, filename + ".tmp")
    fin = open(filename + ".tmp")
    fout = open(filename, 'w')
    strin = fin.read()
    strin = strin.replace(str, newstr)
    fout.write(strin)
    fin.close()
    fout.close()
    #removing tmp file
    #if os.path.exists(filename+".tmp"):
    #    os.remove(filename+".tmp")
    
#####################################################################################################
#
# delete *.tmp files
#
#####################################################################################################

def removeTempFiles():
    rootdir = 'C:\\eclipse\\workspace\\cpm31\\acceptance.ciscoR6\\PHONE\\POL-CORE'
    filename = "inputAvs.cfg.tmp"
    fileList = findFiles(filename,rootdir)
    for files in fileList:
        os.remove(files)


#####################################################################################################
#
# remove a regex from a file
#
#####################################################################################################

def removeGroupLines(str, filename, newstr, pattern):
    #os.chdir('C:\\eclipse\\workspace\\cpm30\\acceptance.ciscoR6\\LTE\\POL-COMMON\\POL-COMMON-002')
    #create temp file
    os.rename(filename, filename + ".tmp")
    fin = open(filename + ".tmp")
    fout = open(filename, 'w')
    strin = fin.read()
    #pattern = re.compile('AVS::Dia-Attr-CiscoGxR6.0v10-Service-Status MULTI\n*7-A-ACT\n*\n*\nEND AVS')
#    strin = re.sub(r'AVS::Dia-Attr-CiscoGxR6.0v10-Service-Status MULTI*\n*7-A-ACT*\n*\n*\n*END AVS', "", strin)
    strin = re.sub(pattern, "", strin)
    #strin = strin.replace(str,newstr)
    fout.write(strin)
    fin.close()
    fout.close()
    #removing tmp file    #if os.path.exists(filename+".tmp"):
    #    os.remove(filename+".tmp")

