##SVN 1.00
##Author: Alex Merriam
##Date: 01-21-2024
##------------------------------------------------------------------
##Notes: Initial API implementation for Raum Application Server. 
##------------------------------------------------------------------
import json
def hub(configArray={'motd':None,'arch':None,'version':'Unset','active_modes':[None, None, None]}, 
       addons={'utilities':{'contact':'Contact other users',
                             'download':'Download remote data for local execution',
                             'invoke':'Locally execute remote data',
                             'license':'Send license request'},
                'features':{}
               }
        ):
    return({'utilities':addons['utilities'],
            'notifications':{'messages':[0]},
            'remote':{'suicide':{'data usage':'high','data charge':10},
                      'floor it':{'data usage':'low','data charge': 2},
                      'detonate grenades':{'data usage':'medium','data charge': 6},
                      'ping':{'data usage':'low','data charge': 1}},
            'version':str(configArray['version']),
            'license':'',
            'carrier':{'public':{'debug':str(configArray['active_modes'][0]),
                                 'safemode':str(configArray['active_modes'][1]),
                                 'tracing':str(configArray['active_modes'][2]),
                                 'addons':addons['features'],
                                 'supported_architectures':json.loads(configArray['arch']),
                                 'related_carriers':json.loads(configArray['carriers'])}}
            }
            )
def licenseset(configArray={'carriers':'undefined'}):
    return({'license':'12345-abcde-09876-zyxwv',
            'neighbors':configArray['carriers']})