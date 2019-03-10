
from model_setup import init_learner_in_loop
from app_setup import init_app
from image_analyzer import setup_image_analyzer
from config import host,port

learn = init_learner_in_loop()
app = init_app()
setup_image_analyzer(app, learn)

if __name__ == '__main__':
    import uvicorn, sys
    if 'serve' in sys.argv: uvicorn.run(app=app, host=host, port=port)
