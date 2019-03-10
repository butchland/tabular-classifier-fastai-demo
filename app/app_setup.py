
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from pathlib import Path

from config import enable_index_page

path = Path(__file__).parent

def init_app():
    app = Starlette()
    app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
    if enable_index_page:
        app.mount('/static', StaticFiles(directory='app/static'))
        app.add_route('/',index,methods=["GET"])
    return app

def index(request):
    html = path/'view'/'index.html'
    return HTMLResponse(html.open().read())

__all__ = ['init_app','path']