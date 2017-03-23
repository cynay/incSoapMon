#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Used to monitor Icognitos ACS servers through its SOAP interface
    
    Python Version: 3.6
"""

__author__ = "Yannic Schneider"
__copyright__ = "Copyright 2017, cYn"
__license__ = "WTFPL"
__version__ = "0.1"
__maintainer__ = "Yannic Schneider"
__email__ = "v@vendetta.ch"
__status__ = "Pre-Production"

###############################################################################
# CODE
###############################################################################

import sys
import logging
from suds.client import Client
from suds import WebFault

# Debugging and Logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.INFO)
logging.getLogger('suds.xsd.schema').setLevel(logging.INFO)
logging.getLogger('suds.wsdl').setLevel(logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


# Globals
authWSDL = 'http://localhost:8899/webservice/IncSecurity?wsdl'
mainWSDL = 'http://localhost:8899/webservice/IncService?wsdl'

user = 'administrator'
passwd = user

def main():
    """Main entry point for the script."""
    authClient = Client(authWSDL, cache=None)
    log.debug(authClient)
    
    res = authClient.service.login(user, passwd)
    log.debug(res)
    
    # Validate response
    if res['errorCode']['hasError'] == False:
        log.info('Login OK')
        
        mainClient = Client(mainWSDL, cache=None)
        log.debug(mainClient)
        
        token = res['authorizationToken']['token']
        log.info('Token: ' + token)
        
        authInfo = mainClient.factory.create('ns2:authorizationInfo')
        authInfo.authorizationToken.token = token
        log.debug(authInfo)
        
        doSoapRequest(mainClient, authInfo, 'getServerOperatingSystemInfo')
        
        
    
def doSoapRequest(client, authInfo, methodName):
    """Return the response/reply of the SOAP request"""
    try:
        reply = getattr(client.service, methodName)(authInfo)
        log.debug(reply)
        return reply
    except WebFault as e:
        log.WARNING('Request error!')
        print(e)
        return -1
        


if __name__ == '__main__':
    sys.exit(main())
