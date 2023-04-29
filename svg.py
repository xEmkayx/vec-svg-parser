import math


class SVG(object):

    """
    Provides methods for creating an empty SVG drawing, adding various
    shapes and text, and saving the finished file.
    """

    def __init__(self):

        """
        Create a few attributes with default values,
        and initialize the templates dictionary.
        """

        self.svg_list = []
        self.width = 0
        self.height = 0

        self.templates = self.__generate_templates()

    def __add_to_svg(self, text):

        """
        Utility function to add element to drawing.
        """

        self.svg_list.append(str(text))

    def __generate_templates(self):

        """
        Create a set of templates for each element type for use by
        methods creating each of these types.
        """

        templates = {}

        # templates["create"] = "<svg width='{}px' height='{}px' viewBox='0 0 {} {}' xmlns='http://www.w3.org/2000/svg' version='1.1' xmlns:xlink='http://www.w3.org/1999/xlink'>\n"
        templates["create"] = "<svg width='100%' height='100%' viewBox='0 0 {} {}' xmlns='http://www.w3.org/2000/svg' version='1.1' xmlns:xlink='http://www.w3.org/1999/xlink'>\n"
        templates["translate"] = " <g transform='translate({},{}) scale(1,-1)'>\n"
        templates["finalize"] = " </g>\n</svg>"
        templates["circle"] = "    <circle stroke='{}' stroke-width='{}px' fill='{}' r='{}' cy='{}' cx='{}' />\n"
        templates["line"] = "    <line stroke='{}' stroke-width='{}px' y2='{}' x2='{}' y1='{}' x1='{}' />\n"
        templates["rectangle"] = "    <rect fill='{}' stroke='{}' stroke-width='{}px' width='{}' height='{}' y='{}' x='{}' ry='{}' rx='{}' />\n"
        templates["text"] = "    <text x='{}' y = '{}' font-family='{}' stroke='{}' fill='{}' font-size='{}px'>{}</text>\n"
        templates["ellipse"] = "    <ellipse cx='{}' cy='{}' rx='{}' ry='{}' fill='{}' stroke='{}' stroke-width='{}' />\n"
        templates["path"] = "    <path d='M {}, {} A {}, {} {} {},{} {}, {}' stroke='{}' fill='{}' stroke-width='{}' />\n"

        return templates

    # def create(self, width, height):
    def create(self, width, height):

        """
        Adds the necessary opening element to document.
        """
        # width = 1920
        # height = 1080

        self.width = width
        self.height = height

        self.svg_list.clear()

        self.__add_to_svg(self.templates["create"].format(width + 50, height))
        self.__add_to_svg(self.templates['translate'].format(width*0.1, height))  # 50, height

    def finalize(self):

        """
        Closes the SVG element.
        """

        self.__add_to_svg(self.templates["finalize"])

    def circle(self, stroke, strokewidth, fill, r, cx, cy):

        """
        Adds a circle using the method's arguments.
        """

        self.__add_to_svg(self.templates["circle"].format(stroke, strokewidth, fill, r, cy, cx))

    def line(self, stroke, strokewidth, x1, y1, x2, y2):

        """
        Adds a line using the method's arguments.
        """

        self.__add_to_svg(self.templates["line"].format(stroke, strokewidth, y2, x2, y1, x1))

    def rectangle(self, width, height, x, y, fill, stroke, strokewidth, radiusx, radiusy):

        """
        Adds a rectangle using the method's arguments.
        """

        self.__add_to_svg(self.templates["rectangle"].format(fill, stroke, strokewidth, width, height, y, x, radiusy, radiusx))

    def fill(self, Fill):

        """
        Fills the entire drawing with specified Fill.
        """

        self.rectangle(self.width, self.height, 0, 0, Fill, Fill, 0, 0, 0)

    def text(self, x, y, fontfamily, fontsize, fill, stroke, text):

        """
        Adds text using the method's arguments.
        """

        self.__add_to_svg(self.templates["text"].format(x, y, fontfamily, stroke, fill, fontsize, text))

    def ellipse(self, cx, cy, rx, ry, fill, stroke, strokewidth):

        """
        Adds ellipse using the method's arguments.
        """

        self.__add_to_svg(self.templates["ellipse"].format(cx, cy, rx, ry, fill, stroke, strokewidth))

    def path(self, x1, y1, rx, ry,
             rot_x: int = 0, large_arc: int = 0, counter_clockwise: int = 1,
             x2: int = 0, y2: int = 0,
             fill: str = 'none', stroke: str = '#000000', strokewidth: int = 1):

        """
        Adds a path using the method's arguments.
        """

        self.__add_to_svg(self.templates["path"].format(x1, y1, rx, ry, rot_x,
                                                        large_arc, counter_clockwise, x2, y2,
                                                        stroke, fill, strokewidth))

    def __str__(self):

        """
        Returns the entire drawing by joining list elements.
        """

        return "".join(self.svg_list)

    def save(self, path):

        """
        Saves the SVG drawing to specified path.
        Let any exceptions propagate up to calling code.
        """

        f = open(path, "w+")
        f.write(str(self))
        f.close()


"""
function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
  var angleInRadians = (angleInDegrees-90) * Math.PI / 180.0;

  return {
    x: centerX + (radius * Math.cos(angleInRadians)),
    y: centerY + (radius * Math.sin(angleInRadians))
  };
}"""


def polar_to_cartesian(cx, cy, radius, angle, neg_flag):
    # angle_rad = (90 - angle) * math.pi / 180.0
    angle_rad = math.radians(angle)
    svg_angle = (angle_rad * 180 / math.pi) + 90
    # angle_rad = (270 - angle) * math.pi / 180.0

    x = cx + (radius * math.cos(svg_angle))
    y = cy + (radius * math.sin(svg_angle))
    return [x, y]
