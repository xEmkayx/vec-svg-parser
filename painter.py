import turtle
import time


main_turtle = turtle.Turtle()


def circle(l_rad: list, l_w: list):
    if int(l_rad[0]) < 0:
        print('kleiner')
    print('circle')


def normal_circle(rx, ry):
    if rx == ry:
        main_turtle.circle(rx)
    else:
        print('Scheiße')
        main_turtle.circle(rx)


def draw_line(x, y):
    main_turtle.pendown()
    main_turtle.goto(x, y)


def move(x, y):
    main_turtle.penup()
    main_turtle.goto(x, y)
    main_turtle.pendown()


def set_screen_size(width_x, width_y):
    turtle.screensize(width_x + 20, width_y + 20)
    print(turtle.screensize())


def finish():
    turtle.done()
    time.sleep(20)


def main():
    pass


if __name__ == '__main__':
    main()
