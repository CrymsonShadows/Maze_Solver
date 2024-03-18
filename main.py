from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 5, 5, 50, 50, win)
    win.wait_for_close()

main()
