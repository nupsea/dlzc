import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor


input_size = 299

classes = [
    'dress',
    'hat',
    'longsleeve',
    'outwear',
    'pants',
    'shirt',
    'shoes',
    'shorts',
    'skirt',
    't-shirt'
]


interpreter = tflite.Interpreter(model_path='xception_v5_14_0.897.keras.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

preprocessor = create_preprocessor('xception', target_size=(input_size, input_size))


url = 'http://bit.ly/mlbookcamp-pants'

def predict(url):
    X = preprocessor.from_url(url) 

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()

    preds = interpreter.get_tensor(output_index)

    res = dict(zip(classes, preds[0]))
    # pred_clothing = max(res.items(), key=lambda x: x[1])

    res = {k: float(v) for k, v in res.items()}

    return res

def lambda_handler(event, context):
    url = event['url']
    response = predict(url)
    return response