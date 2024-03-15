from graphics import Point, Line, Window
from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            maze_col = []
            for j in range(self._num_rows):
                maze_col.append(Cell(self._win))
            self._cells.append(maze_col)
        for col in range(len(self._cells)):
            for row in range(len(self._cells[col])):
                self._draw_cell(row, col)
    
    def _draw_cell(self, i, j):
        cell = self._cells[j][i]
        cell._x1 = self._x1 + self._cell_size_x * j
        cell._x2 = cell._x1 + self._cell_size_x
        cell._y1 = self._y1 + self._cell_size_y * i
        cell._y2 = cell._y1 + self._cell_size_y
        cell.draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)
