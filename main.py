from graphics import Window, Point, Line, Cell

def main():
    win = Window(800, 600)
    line = Line(Point(20, 20), Point(20, 360))
    win.draw_line(line, "black")
    cell = Cell(win, 10, 10, 60, 60)
    cell.draw()
    cell = Cell(win, 30, 30, 80, 80, left=False)
    cell.draw()
    cell = Cell(win, 40, 40, 90, 90, left=False, top=False, bottom=False)
    cell.draw()
    win.wait_for_close()

main()