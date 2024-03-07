from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    line = Line(Point(20, 20), Point(20, 360))
    win.draw_line(line, "black")
    win.wait_for_close()

main()