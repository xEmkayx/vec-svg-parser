class Color:
    def __init__(self):
        self.current_color = 'black'

    def get_colors(self, i: int = 2):
        col = 'black'
        match i:
            case 1:
                col = 'black'
            case 2:
                col = 'green'
            case 3:
                col = 'red'
            case 4:
                col = 'yellow'
            case 5:
                col = 'blue'
            case _: col = 'black'
        self.set_color(col)
        return col

    def set_color(self, col):
        self.current_color = col


color = Color()
