
level = {'CRITICAL':50, 'ERROR':40, 'WARNING':30, 'INFO':20, 'DEBUG':10, 'NOTSET':0}

def log_name2level(levelname):
    return level[levelname.upper()] if (levelname.upper() in level) else level['NOTSET']    
