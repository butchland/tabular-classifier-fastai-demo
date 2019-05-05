from logging import getLogger

from utils import log_name2level
from model_setup import init_learner_in_loop
from app_setup import init_app
from input_analyzer import setup_input_analyzer
from config import host,port, log_level

logger = getLogger()
logger.setLevel(log_name2level(log_level))

learn = init_learner_in_loop()
app = init_app()
setup_image_analyzer(app, learn)

if __name__ == '__main__':
    import uvicorn, sys
    if 'serve' in sys.argv: uvicorn.run(app=app, host=host, port=port, log_level=log_level)
