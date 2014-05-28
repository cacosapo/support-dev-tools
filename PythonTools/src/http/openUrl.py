'''
Created on 11/04/2012

@author: lucask
'''
import os

def printOptions(list):
        for idx, val in enumerate(list):
            index = idx + 1
            print str(index) + " - " + val

if __name__ == '__main__':

    prog = "\"C:/Program Files (x86)/Mozilla Firefox/firefox.exe\" "
    prefix = "http://zbor.openet-telecom.lan/~"
    sufix = "/newreport/"
    tester3 = "http://zbor.openet-telecom.lan/~tester3/newreport/"
    listOptions = ["tester3","roger","lucask","luisy","dennisf"] 
    list = []

#   Populate the listOptions
    for opt in listOptions:
        list.append(prefix+opt+sufix)
    
#    for idx, val in enumerate(listOptions):
#        index = idx + 1
#        print str(index) + " - " + val
        
    option = 1
    while (option != 0):
        printOptions(listOptions)
        try:
            option = int(input("selecione o ambiente:"))
        except:
            option = -1
            print "opcao invalida"
            continue
        if (option > len(list)):
            print "out of range"
            continue
        os.system(prog + list[option-1])
        print "Browser aberto com sucesso"