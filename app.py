import os
import cv2
import json
import base64
import config
import numpy as np
from utils import generate_dataset_festures, predict_people
from flask import Flask, request, render_template, jsonify
# from flask_socketio import SocketIO, emit

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

generate_dataset_festures()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-name', methods=['POST'])
def submit_name():
    if request.method == 'POST':
        name = request.form['name'].lower()
        if name not in os.listdir(config.data_dir):
            return "SUCCESS"
        return "FAILURE"
        
@app.route('/submit-photos', methods=['POST'])
def submit_photos():
    if request.method == 'POST':
        name = request.form['name'].lower()
        images = json.loads(request.form['images'])

        os.mkdir(os.path.join(config.data_dir, str(name)))

        person_directory = os.path.join(config.data_dir, name)
        for i, image in enumerate(images):
            image_numpy = np.fromstring(base64.b64decode(image.split(",")[1]), np.uint8)
            image = cv2.imdecode(image_numpy, cv2.IMREAD_COLOR)
            cv2.imwrite(os.path.join(person_directory, str(i) + '.png'), image)
        
        generate_dataset_festures()

        return "results"

@app.route("/results")
def results():
    return render_template("results.html")

@app.route("/predict-frame", methods=['POST'])
def predict_frame():
    if request.method == 'POST':
        image = request.form['image']
        image_numpy = np.fromstring(base64.b64decode(image.split(",")[1]), np.uint8)
        image = cv2.imdecode(image_numpy, cv2.IMREAD_COLOR)

        image = predict_people(image)

        retval, buffer = cv2.imencode('.png', image)
        img_as_text = base64.b64encode(buffer)

        return img_as_text




if __name__ == "__main__":
    app.run(debug=False)
