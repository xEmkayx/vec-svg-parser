import copy
import painter_svg
import filenames
import colors
from colors import color
import argparse


def parse_file(filename, online: bool = False) -> list:
    if online:
        # lines = filename.read()
        lines = filename.readlines()
        # for line in lines:
        #    print(line.decode())
        # print(lines)
        # for idx, i in enumerate(lines):
        for idx, i in enumerate(lines):
            # print(idx, i)
            i = i.decode()
            i = i.strip('\n')
            a = i.split(' ')
            lines[idx] = a

    else:
        with open(filename, 'r') as f:
            lines = copy.copy(f.readlines())
            for idx, i in enumerate(lines):
                i = i.strip('\n')
                a = i.split(' ')
                lines[idx] = a

    return lines


def parse(input_filename, output_filename: str = filenames.output_file, online: bool = False):
    lines = parse_file(input_filename, online)
    previous_coords = [0, 0]
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
                    painter_svg.finish(output_filename)
                    # return r
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-file", help="Path to the input file", required=True)
    parser.add_argument("-o", "--output-file", help="The output filename (filename only!)", required=True)
    args = parser.parse_args()

    parse(input_filename=args.input_file, output_filename=args.output_file, online=False)


if __name__ == '__main__':
    main()
