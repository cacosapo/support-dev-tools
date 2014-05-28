'''
Created on 05/04/2012

@author: lucask
'''
import re

def replaceRegex(replace, pattern,text):
    p = re.compile(pattern)
    return p.sub( replace, text)

if __name__ == '__main__':
#    p = re.compile( "(^b\Z|white|red|shoes\n(\W*)teste)")
#    print p.sub( 'colour', 'blue socks and red shoes\n   teste')
#    p.sub( 'colour', 'blue socks and red shoes', count=1)
    replace = '    colour'
    pattern = "\
    ((.*)Subscription(.*)\n\
    (.*)END_USER_E164(.*)\n\
    (.*)\n\
    (.*)END AVS(.*))"
    sample = '''\
    AVS::Dia-Attr-Subscription-Id MULTI
        Subscription-Id-Type END_USER_E164
        Subscription-Id-Data [Lb_GetMINDConfig "LTE_MSISDN_POL-MRC-ST-SST-021"]
    END AVS
    AVS::Dia-Attr-Subscription-Id MULTI
        Subscription-Id-Type END_USER_IMSI
        Subscription-Id-Data [Lb_GetMINDConfig "LTE_IMSI_POL-MRC-ST-SST-021"]
    END AVS
    Destination-Host [GetTargetProperty "SyDestinationHost"]
    Called-Station-Id broadband
    Destination-Realm [GetTargetProperty "SyDestinationRealm"]
    AVS::Dia-Attr-Openet-Service-Parameter MULTI
        Openet-Service-Parameter-Name ROAMING_ZONE
        Openet-Service-Parameter-Value On-Net
    END AVS
    '''

    print replaceRegex(replace, pattern, sample)