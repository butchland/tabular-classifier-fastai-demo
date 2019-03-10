from starlette.responses import JSONResponse
from functools import partial

from image_handler import get_uploaded_image
from config import handle_prediction, prediction_api_path, api_response_key_name

def make_image_analyzer(image_learner):
    async def analyze_image(request):
        img = await get_uploaded_image(request)
        prediction, index, probabilities = image_learner.predict(img)
        result = handle_prediction(prediction, index, probabilities)
        return JSONResponse({api_response_key_name: result})
    return analyze_image

def setup_image_analyzer(app, image_learner):
    make_meta_analyzer = partial(make_image_analyzer, image_learner=image_learner)
    app.add_route(prediction_api_path, make_meta_analyzer(), methods=['POST'])


__all__ = ['setup_image_analyzer']