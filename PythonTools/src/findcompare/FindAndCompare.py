'''
Created on 07/03/2012

@author: lucask
'''
import urllib2
from bs4 import BeautifulSoup
import os
import re


#####################################################################################################
#
# Create expected and actual file with specific avps inside
#
#####################################################################################################

def findStringUrl(url,string):
    print 'start findStringUrl'
    
    avpexpected = string+':Expected'
    avpactual = string+':Actual'
    fexpected = open('expected.txt', 'w')
    factual = open('actual.txt', 'w')

    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    document = response.read()

    soup = BeautifulSoup(document)
    tabela = soup.find('table')

    lista = tabela.findAll('td')

    for elem in lista:
        if avpexpected in str(elem):
        #print elem
            fexpected.write(str(elem))
        if avpactual in str(elem):
        #print elem
            factual.write(str(elem))

    #close files
    fexpected.close()
    factual.close()
    
    print 'end findStringUrl'
    
    return

#####################################################################################################
#
#
#
#####################################################################################################

def runCommand(cmd):
    print 'start runCommand'
    os.system(cmd)
    print 'end runCommand'
    return

#####################################################################################################
#
#
#
#####################################################################################################

def removeLineTest(str):
    os.chdir('C:\\eclipse\\workspace\\cpm30\\acceptance.ciscoR6\\LTE\\POL-COMMON\\POL-COMMON-002')
    #create temp file
    os.rename('inputAvs.cfg', 'inputAvs.cfg.tmp')
    fin = open('inputAvs.cfg.tmp')
    fout = open('inputAvs.cfg', 'w')
    for line in fin.readlines():
        if re.search(str, line, re.IGNORECASE) == None:       
            fout.write(line)
    fin.close()
    fout.close()
    #removing tmp file
    if os.path.exists('inputAvs.cfg.tmp'):
        os.remove('inputAvs.cfg.tmp')
