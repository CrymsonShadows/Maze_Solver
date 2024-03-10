from graphics import Point, Line, Window

class Cell:
    def __init__(self, win: Window, x1, y1, x2, y2, left=True, right=True, top=True, bottom=True, fill_color="black") -> None:
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self.fill_color = fill_color
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line, self.fill_color)
        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, self.fill_color)
        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line, self.fill_color)
        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, self.fill_color)