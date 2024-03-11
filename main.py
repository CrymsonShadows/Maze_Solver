from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win, 50, 50, 100, 100)
    cell1.draw()
    cell2 = Cell(win, 100, 50, 150, 100)
    cell2.draw()
    cell3 = Cell(win, 150, 50, 200, 100)
    cell3.draw()
    cell4 = Cell(win, 150, 0, 200, 50)
    cell4.draw()
    cell1.draw_move(cell2)
    cell2.draw_move(cell3, True)
    cell3.draw_move(cell4)
    win.wait_for_close()

main()