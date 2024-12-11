
import tflite_runtime.interpreter as tflite

import numpy as np
from io import BytesIO
from urllib import request

from PIL import Image

# For HW model
model_path = 'model_2024_hairstyle'


interpreter = tflite.Interpreter(model_path=f'{model_path}.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img
    


def prepare_input(x):
    return x / 255

def pre_process(img_url):
    raw_img = download_image(img_url)
    img = prepare_image(raw_img, target_size=(200, 200))

    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = prepare_input(X)
    
    return X


def predict(url):
    X = pre_process(url)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()

    pred = interpreter.get_tensor(output_index)
    return pred

def lambda_handler(event, context):
    url = event['url']
    response = predict(url)
    return response

