from starlette.responses import JSONResponse
from functools import partial
import logging

from input_handler import extract_input
from config import handle_prediction, prediction_api_path, api_response_key_name, log_level

logger = logging.getLogger()

debug = False
if log_level == 'debug':
    debug = True

def make_input_analyzer(learner):
    async def analyze_input(request):
        input = await extract_input(request)
        prediction, index, probabilities = learner.predict(input)
        result = handle_prediction(prediction, index, probabilities)
        response = JSONResponse({api_response_key_name: result})

        if debug:
            logger.debug('response status: {}'.format(response.status_code))
            logger.debug('response mediatype: {}'.format(response.media_type))
            logger.debug('response headers: {}'.format(response.headers))
            logger.debug('response body: {}'.format(response.body))

        return response
        
    return analyze_input

def setup_input_analyzer(app, learner):
    make_meta_analyzer = partial(make_input_analyzer, learner=learner)
    app.add_route(prediction_api_path, make_meta_analyzer(), methods=['POST'])


__all__ = ['setup_input_analyzer']