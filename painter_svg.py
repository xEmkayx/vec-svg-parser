# import cairo
import math
import copy

import colors
from colors import color
import svg
import filenames
# import svgwrite

with open(filenames.input_file, 'r') as f:
    lines = copy.copy(f.readlines())
    i = 0
    for idx, line in enumerate(lines):
        if line.split(' ')[0] == 'ob':
            i = idx
            break

    width = int(lines[i].split(' ')[i].split(',')[2])
    height = int(lines[i].split(' ')[i].split(',')[3])

s = svg.SVG()
s.create(width, height)


def parse_file() -> list:
    with open(filenames.input_file, 'r') as f:
        lines = copy.copy(f.readlines())
        for idx, i in enumerate(lines):
            i = i.strip('\n')
            a = i.split(' ')
            lines[idx] = a
        return lines


def el(p, r1, r2):
    x, y = p
    s.path(x, y, r1, r2)


def es(p, r1, r2, w1=0, w2=360):
    # print(f'p: {p}, r1: {r1}, r2: {r2}, w1: {w1}, w2: {w2}')

    large_flag = 1 if w2 - w1 > 180 else 0
    sweep_flag = 0 if r1 < 0 else 1

    if w1 > w2:
        w1, w2 = w2, w1

    if r1 < 0:
        r1 *= -1

    apx, apy, epx, epy = ellipse_arc_points(p[0], p[1], r1, r2, w1, w2)
    # print(f'apx: {apx}, apy: {apy}, epx: {epx}, epy: {epy}')

    # determine sweep flag based on sign of r1
    sweep_flag = 0 if r1 < 0 else 1
    large_flag = 1 if w2 - w1 > 180 or w1-w2 > 180 else 0

    # create path element for ellipse
    s.path(apx, apy, r1, r2, counter_clockwise=sweep_flag, large_arc=large_flag,
           x2=epx, y2=epy, stroke=color.current_color)


def ellipse_arc_points(x0, y0, a, b, theta1, theta2):
    # Convert angles to radians
    theta1 = math.radians(theta1)
    theta2 = math.radians(theta2)

    # Calculate polar coordinates of arc points
    def r(t): return a * b / math.sqrt((b * math.cos(t)) ** 2 + (a * math.sin(t)) ** 2)

    def x(t): return x0 + r(t) * math.cos(t)

    def y(t): return y0 + r(t) * math.sin(t)

    # Calculate Cartesian coordinates of arc points
    x1, y1 = x(theta1), y(theta1)
    x2, y2 = x(theta2), y(theta2)

    return x1, y1, x2, y2


def draw_line(x1, y1, x2, y2, line_width: int = 1):
    col = color.current_color
    print(f'color line: {col}')
    s.line(stroke=col, strokewidth=line_width, x1=x1, y1=y1, x2=x2, y2=y2)


def finish(filename: str = 'output'):
    s.finalize()
    try:
        s.save(f'{filename}.svg')
    except IOError as ioe:
        print(ioe)
    finally:
        print(s)
