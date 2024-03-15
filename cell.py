from graphics import Point, Line, Window

class Cell:
    def __init__(self, win=None, x1=None, y1=None, x2=None, y2=None, left=True, right=True, top=True, bottom=True, fill_color="black") -> None:
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self.fill_color = fill_color
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.__win = win

    def draw(self):
        if self.__win is None:
            return
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self.__win.draw_line(line, self.fill_color)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self.__win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self.__win.draw_line(line, self.fill_color)
        else:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self.__win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self.__win.draw_line(line, self.fill_color)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self.__win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self.__win.draw_line(line, self.fill_color)
        else:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self.__win.draw_line(line, "white")

    # def draw(self, x1, y1, x2, y2):
    #     self._x1 = x1
    #     self._x2 = x2
    #     self._y1 = y1
    #     self._y2 = y2
    #     if self.has_left_wall:
    #         line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
    #         self.__win.draw_line(line, self.fill_color)
    #     if self.has_right_wall:
    #         line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
    #         self.__win.draw_line(line, self.fill_color)
    #     if self.has_top_wall:
    #         line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
    #         self.__win.draw_line(line, self.fill_color)
    #     if self.has_bottom_wall:
    #         line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
    #         self.__win.draw_line(line, self.fill_color)

    def draw_move(self, to_cell, undo=False):
        fill_color = ""
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        self_x_mid = (self._x2 - self._x1) // 2 + self._x1
        self_y_mid = (self._y2 - self._y1) // 2 + self._y1
        to_x_mid = (to_cell._x2 - to_cell._x1) // 2 + to_cell._x1
        to_y_mid = (to_cell._y2 - to_cell._y1) // 2 + to_cell._y1
        line = Line(Point(self_x_mid, self_y_mid), Point(to_x_mid, to_y_mid))
        self.__win.draw_line(line, fill_color)