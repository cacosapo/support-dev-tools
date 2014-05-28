'''
Created on 07/03/2012

@author: lucask
'''
import os

#####################################################################################################
#
#
#
#####################################################################################################
def transfer():
    fromPath = ""
    toPath = ""
    fileTransfer = ""
    cmd = "WinSCP /script=../scripts/upload.txt /parameter " + fromPath + toPath + fileTransfer
    os.system(cmd)
    