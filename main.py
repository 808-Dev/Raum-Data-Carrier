##SVN 1.00
##Author: Alex Merriam
##Date: 01-21-2024
##Credit: Raum API - /main.py
##------------------------------------------------------------------
##Notes: Initial API implementation for Raum Application Server. 
##------------------------------------------------------------------ 

## Import modules safely into the current server instance. Otherwise throw an error and exit.
try:
    import sys, configparser
    if('--debug' in sys.argv or '-d' in sys.argv):
        print('Raum Application Server starting in debugging mode.')
        debug = True
    else:
        debug = False

    if('--abuse' in sys.argv or '-a' in sys.argv):
        print('Raum Application Server starting in tracking mode.')
        trace = True
    else:
        trace = False

    if('--safemode' in sys.argv or '-s' in sys.argv):
        print('Raum Application Server starting in safe mode.')
        safemode = True
    else:
        safemode = False
    
    #if('--config' in sys.argv or '-c' in sys.argv):


    if(len(sys.argv) == 1 ):
        print('Raum Application Server starting in normal mode.')
    if('--help' in sys.argv or '-h' in sys.argv):
        print('Arguments:\n'+
              '--debug,    -d   -   Start server in debug mode.\n'+
              '--safemode, -s   -   Start server in safe mode. (Starts server without additional addon packages)\n'+
              '--abuse,    -a   -   Start server in abusive IP tracing mode.\n'+
              '--help,     -h   -   Display this help file and ends the initialized instance.\n\n'+
              '--config,   -c   -   Show current active configuration\n\n'+
              'Usage:\n'+
              'raumserv [-d][-s][-a][-h]\n'+
              'raumserv [--debug][--safemode][--abuse][--help]\n')
        sys.exit('Closing Server: Help documents accessed.')
except ImportError as importException:
    sys.exit('Native library import error: ' + str(importException))

try:
    #from colorama import Fore, Back, Style
    import sys, uvicorn, os
    from libraries.handlers.module import *
    from fastapi import FastAPI, HTTPException, Depends, UploadFile
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
    from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
    from fastapi.responses import HTMLResponse, FileResponse
    from typing import Union
except ImportError as importException:
    if(debug==True):
        raise Exception('Required library import error: ' + str(importException))
    sys.exit('Required library import error: ' + str(importException))

try:
    from libraries.plugins.module import *
    from libraries.native.module import *
except ImportError as importException:
    if(debug == True):
        raise Exception(f'Addon: {str(importException.name)}\n\nException: {str(importException)}')
    else:
        print(f'Critical import error: {str(importException.name)} - Error will be further explained in debug mode.')

try:
    from patches.database.module import *
except ImportError as importException:
    if(debug == True):
        raise Exception(f'Patch: {str(importException.name)}\n\nException: {str(importException)}')
    else:
        print(f'Critical patch import error: {str(importException.name)} - ignoring module but usually this breaks critical functions. (Restart in debug mode)')

app = FastAPI(title="Raum Application Server", description="This project is currently in development and will have issues.", version="24.01", terms_of_service='', summary="This is the official server for Raum")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
oauth2_schema = OAuth2PasswordBearer(tokenUrl="authorize")

os.system('cls' if os.name == 'nt' else 'clear')

## Define all data from config file.

globalconfig = configparser.ConfigParser()
globalconfig.read('config.ini')
creds = {'user':globalconfig.get('database', 'username'),
         'pasword':globalconfig.get('database', 'password'),
         'host':globalconfig.get('database', 'address'),
         'db':globalconfig.get('database', 'database')}

## Define the API routes for Raum.

@app.get("/", tags=["Hub"], summary="This is the main hub point for Raum to send user data to.")
async def displayhub(): 
    configArray = {'motd':globalconfig.get('broadcast_config', 'motd'),
                   'arch':globalconfig.get('broadcast_config', 'compatible_architecture'),
                   'carriers':globalconfig.get('broadcast_config', 'approved_carrier_points'),
                   'version':globalconfig.get('broadcast_config','version'),
                   'active_modes':[debug, trace, safemode]}
    return hub(configArray)

@app.get("/license", tags=["Licensing"], summary="This allows users to request licenses from the carrier.")
async def displaylicense(): 
    return licenseset({'carriers':json.loads(globalconfig.get('broadcast_config', 'approved_carrier_points'))})

@app.get("/contact", tags=["Contacts"], summary="This allows users to request licenses from the carrier.")
async def displaycontactlist(): 
    return licenseset({'carriers':json.loads(globalconfig.get('broadcast_config', 'approved_carrier_points'))})

