
from fastai.tabular import load_learner
from pathlib import Path
import aiohttp, asyncio

from config import model_file_name, model_file_download_url

path = Path(__file__).parent
model_path = path/'models'

def init_learner_in_loop():
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(setup_learner())]
    learner = loop.run_until_complete(asyncio.gather(*tasks))[0]
    loop.close()
    return learner

async def setup_learner():
    await download_file(model_file_download_url, model_path/model_file_name)
    try:
        learner = load_learner(model_path, model_file_name)
        return learner
    except RuntimeError as e:
        if len(e.args) > 0 and 'CPU-only machine' in e.args[0]:
            print(e)
            message = "\n\nThis model was trained with an old version of fastai and will not work in a CPU environment.\n\nPlease update the fastai library in your training environment and export your model again.\n\nSee instructions for 'Returning to work' at https://course.fast.ai."
            raise RuntimeError(message)
        else:
            raise

async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f: f.write(data)

__all__ = ['init_learner_in_loop']