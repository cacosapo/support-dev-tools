'''
Created on 07/03/2012

@author: lucask
'''

import urllib2
from bs4 import BeautifulSoup
import os

#####################################################################################################
#
#
#
#####################################################################################################

def findStringUrl(url):
    avpexpected = 'AAR_UPDATE:Expected'
    avpactual = 'AAR_UPDATE:Actual'
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
    return

#####################################################################################################
#
#
#
#####################################################################################################

url = "http://zbor.openet-telecom.lan/~tester3/newreport//PHONE.PHONE-AC.PHONE-AC-018//PHONE_PHONE_AC_018.act//RunDsdUnitTests_test.dsdu_PMATF_6000000/7table5.html"
findStringUrl(url)

url = "http://zbor.openet-telecom.lan/~tester3/newreport//PHONE.PHONE-AC.PHONE-AC-018//PHONE_PHONE_AC_018.act//RunDsdUnitTests_test.dsdu_PMATF_6000000/"

request = urllib2.Request(url)
response = urllib2.urlopen(request)
document = response.read()
avpexpected = 'AAR_UPDATE:Expected'
avpactual = 'AAR_UPDATE:Actual'
fexpected = open('expected.txt', 'w')
factual = open('actual.txt', 'w')

#command line responsible for comparing files
cmd = 'C:"\Program Files (x86)"\WinMerge\WinMergeU.exe expected.txt actual.txt'

soupRoot = BeautifulSoup(document)
listaDoc = soupRoot.findAll('a')

for doc in listaDoc:
    if '7table' in str(doc.get('href')):
        tempUrl = url+str(doc.get('href'))
        findStringUrl(tempUrl)
#close files
fexpected.close()
factual.close()

#comparing files
os.system(cmd)

