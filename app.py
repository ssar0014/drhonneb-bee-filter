from flask import Flask, jsonify, request, Response
import json
import os
import boto3
from config import S3_BUCKET, S3_KEY, S3_SECRET

import numpy as np
from fastai.vision import image, load_learner, open_image

global s3
s3 = boto3.resource('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)

global learner
path = './'
learner = load_learner(path)

global bee_flag

def bee_not_not():
    image_file = s3.Bucket(S3_BUCKET).download_file('public/user_photo.png', '/tmp/user_photo.png')
    filename = '/tmp/user_photo.jpg'
    im = open_image(filename)
    learner.precompute=False # We'll pass in a raw image, not activations
    preds = learner.predict(im)
    preds = list(preds)
    classes = preds[2].tolist()
    if classes[0] < classes[1]:
        return 'not bee'
    else:
        return 'bee'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getBeeOrNot():
    bee_flag = ''
    # create list for final response
    responses = list()

    # first we check the condition of if the user photo is that of a bee or not
    bee_flag = bee_not_not()
    # attach all the responses to a list and format it as json
    responses.append({'bee_or_not':bee_flag})
    responses = json.dumps({'response':responses})

    # response from the API is sent as a json response
    try:
        return Response(response=responses, mimetype='text/plain', status=200)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug = True)
