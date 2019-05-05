import logging
import pandas as pd
from config import log_level

logger = logging.getLogger()

debug = False
if log_level == 'debug':
    debug = True

CAT_NAMES = ['workclass','education','marital-status',
             'occupation', 'relationship', 'race']
CONT_NAMES = ['age','fnlwgt', 'education-num']

def dict2Series(form_values):
    index = []
    values = []
    for k,v in  form_values.items():
        if k in CAT_NAMES:
            values.append(' ' + v) # artifact of model assumes values have initial space
            index.append(k)
        elif k in CONT_NAMES:
            values.append(float(v))
            index.append(k)
            
    return pd.Series(values,index=index)

async def extract_input(request):
    if debug:
        logger.debug('request method: {}'.format(request.method))
        logger.debug('request url: {}'.format(request.url))
        logger.debug('request headers {}'.format(request.headers))

    data = await request.form()
    form_values = dict(data)
    
    if debug:
        for k,v in form_values.items():
            logger.debug('form \'{}\' : \'{}\''.format(k,v))

    input = dict2Series(form_values)
    return input


__all__ = ['extract_input']