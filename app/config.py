# defaults for server.py (only used for local server)
port = 5042
host = '0.0.0.0'

# config for image prediction api path and if html index page is available
# remember to modify prediction_api_path and api_response_key_name in /static/client.js 
# to match prediction_api_path and api_response_key_name in config
prediction_api_path = '/analyze'
enable_index_page = True
api_response_key_name = 'result'

# configuration for image learner pkl file stored in cloud
# see https://course.fast.ai/deployment_render.html for instructions to generate download urls
# for model files (.pkl) shared on google drive and dropbox
model_file_download_url = 'YOUR-PET-BREED-CLASSIFIER-MODEL-DOWNLOAD-URL'
model_file_name = 'export.pkl'

# configuration for prediction handler
# change this custom.petbreed_prediction_handler into 
# your own custom prediction handler which can be named anything (modify the import)
# as long as this config module exports that method as 'handle_prediction'
from custom.petbreed_prediction_handler import handle_prediction as handle_prediction
