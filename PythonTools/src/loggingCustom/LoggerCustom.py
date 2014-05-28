'''
Created on 29/03/2012

@author: lucask
'''
import logging

class LoggerCustom:
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.FORMAT='%(asctime)s %(lineno)d %(filename)s %(funcName)s %(pathname)s %(message)s '
        self.DATEFORM='%m/%d/%Y %I:%M:%S %p'
        logging.basicConfig(filename='output.log', level=logging.INFO, format=self.FORMAT, datefmt=self.DATEFORM)
        logging.info('Started')
        
    def infoLog(self, msg):
        logging.info(msg)
        
    def warnLog(self, msg):
        logging.warning(msg)
        
    def errorLog(self, msg):
        logging.error(msg)