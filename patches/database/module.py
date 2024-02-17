##SVN 1.00
##Author: Alex Merriam
##Date: 01-21-2024
##------------------------------------------------------------------
##Notes: Initial API implementation for Raum Application Server. 
##------------------------------------------------------------------

import mysql.connector, mysql.connector.errors

def StartDBInstance(creds=(None,None,None,None)):
    if creds or len(creds)==4:
        try:
            Instance = mysql.connector.connect(host=creds['host'], user=creds['user'], password=creds['password'], database=creds['database'])
            return(Instance.cursor(), Instance)
        except mysql.connector.errors.ProgrammingError as exception:
            if exception.errno == 1045:
                return('Invalid credentials')
            elif exception.errno == 1049:
                return('Invalid database')
            else:
                return(f'Error: {exception}')
    else:
        return(f'Malformed credential packet: {creds}')

def DBFunction(functionName=None, arguments=[None], instance=None):
    if functionName != None and arguments != [None] and instance != None:
        DB = instance[0]
        template = 'SELECT {}({});'.format(functionName, ', '.join(['%s']*len(arguments)))
        try:
            DB.execute(template, arguments)
            return(DB.fetchall()[0], instance[1].commit())
        except mysql.connector.Error as err:
            return(f'Exception occured while processing entity.\n\n Exception reason:\n\n{err.errno}')
    else:
        return(f'Malformed function packet: {instance, functionName, arguments}')