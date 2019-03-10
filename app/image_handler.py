
from io import BytesIO
from fastai.vision import open_image

async def get_uploaded_image(request):
    data = await request.form()
    img_bytes = await (data['file'].read())
    img = open_image(BytesIO(img_bytes))
    return img


__all__ = ['get_uploaded_image']