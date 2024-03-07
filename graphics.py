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
