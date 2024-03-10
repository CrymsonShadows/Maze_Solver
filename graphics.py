from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    
class Line:
    def __init__(self, point_1: Point, point_2: Point) -> None:
        self.point_1 = point_1
        self.point_2 = point_2
    
    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("maze_solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while(self.__running):
            self.redraw()
    
    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False

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
        