# Starter for deploying [fast.ai](https://www.fast.ai) models on [Render](https://render.com)

This repo can be used as a starting point to deploy [fast.ai](https://github.com/fastai/fastai) models on Render.

The sample app described here is up at https://fastai-v3.onrender.com. Test it out with bear images!

The guide for production deployment to Render is at https://course.fast.ai/deployment_render.html.

## Refactored Project Template

Heavily modified in order to convert it into a project template for faster deployment of simple image classification projects

## Updated Demo Site

By default it deploys a _Pet Breed Image Classifier_ based on __Lesson 1__ of __Practical Deep Learning for Coders V3__ from the [fast.ai](https://course.fast.ai) course using a Resnet50 shared over Google Drive

## Modifying the template

See __config.py__ and __petbreed_prediction_handler.py__. 

You can upload your own image learner model into google drive or dropbox and the app can download the model into your cloud deployment platform.

Your custom prediction handler can convert the prediction responses from your model into json objects that your api will return to the client web app. 

You can also turn off the web page if you just want to serve an api endpoint that processes an image and returns your custom response (as a json object).

## Accessing the prediction analyzer endpoint

You can also use the app solely as a prediction api provider without providing a default index html page.

Simply set the `enable_index_page` setting in `config.py` to __False__

You can access the api endpoint (using default settings) using the following curl command
```
curl -F "file=@/path/to/your/image/file" <your-url-here>/analyze
```
For example:
```
curl -F "file=@/home/butch/mycute-cat.jpg" localhost:5042/analyze
```


