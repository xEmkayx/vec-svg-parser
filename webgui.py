import time

from flask import Flask, request, render_template, Markup
import os

import painter_svg
import parser
from colors import color

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


@app.route('/editor', methods=['GET', 'POST'])
def web_ide():
    if request.method == 'POST':
        input_text = request.form['input_text']
        svg = parse_online(input_text)
        print(svg)

        return render_template('ide.html', svg_text=Markup(svg))
    else:
        return render_template('ide.html')


def parse_online(text):
    text = text.replace('\r', '')
    lines = [i for i in text.split('\n')]
    for idx, i in enumerate(lines):
        # print(idx, i)
        # i = i.decode()
        i = i.strip('\n')
        a = i.split(' ')
        lines[idx] = a
    previous_coords = [0, 0]
    r = ''
    for idx, line in enumerate(lines):
        match line[0].lower():
            case 'os':
                # print('neues objekt')
                pass
            case 'ob':
                b = line[1].split(',')
                width = float(b[2]) - float(b[0])
                height = float(b[3]) - float(b[1])
                painter_svg.create(width, height)
            case 'oe':
                if idx+1 == len(lines):
                    r = painter_svg.finalize()
            case 'co':
                c = int(line[1].split(',')[0])
                # print(f'color: {c}')
                color.get_colors(c)
            case 'ma':
                s = line[1].split(',')
                x, y = float(s[0].strip()), float(s[1].strip())
                # print(f'x: {x} \t y: {y}')
                previous_coords = [x, y]
            case 'da':
                s = line[1].split(',')
                x, y = float(s[0].strip()), float(s[1].strip())
                painter_svg.draw_line(previous_coords[0], previous_coords[1], x, y)
                previous_coords = [x, y]
            case 'el':
                rad = line[1].split(',')
                x, y = float(rad[0].strip()), float(rad[1].strip())
                painter_svg.el((previous_coords[0], previous_coords[1]), x, y)
                previous_coords = [x, y]
            case 'es':
                rad = line[1].split(',')
                w = line[2].split(',')

                r1, r2 = float(rad[0].strip()), float(rad[1].strip())
                w1, w2 = int(w[0].strip()), int(w[1].strip())
                painter_svg.es((previous_coords[0], previous_coords[1]), r1, r2, w1, w2)
            case _:
                pass
                # print(0)
    return r


if __name__ == '__main__':
    app.run()
