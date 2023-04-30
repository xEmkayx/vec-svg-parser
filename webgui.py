import time

from flask import Flask, request, render_template
import os

import parser

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    output_name = os.path.abspath('static/IMG/adv.svg')
    img = os.path.join(app.config['UPLOAD_FOLDER'], 'adv.svg')
    if request.method == 'POST':
        input_file = request.files['input_file']
        output_name = request.form['output_name']
        parser.parse(input_file, output_name, True)
        print(f'img output name: {output_name}')
        img = os.path.join(app.config['UPLOAD_FOLDER'], f'{output_name}.svg')

    print('exists?: ', os.path.exists(img))
    while not os.path.exists(img):
        time.sleep(0.5)

    print(f'output: {img}')
    return render_template('index.html', user_image=img)


if __name__ == '__main__':
    app.run()
