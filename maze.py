from graphics import Point, Line, Window
from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        for _ in range(self._num_cols):
            maze_col = []
            for _ in range(self._num_rows):
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

    def _break_walls_r(self, col, row):
        self._cells[col][row].visited = True
        while True:
            to_visit = []
            if col > 0 and self._cells[col - 1][row].visited is False:
                to_visit.append((col - 1, row))
            if col < self._num_cols - 1 and self._cells[col + 1][row].visited is False:
                to_visit.append((col + 1, row))
            if row > 0 and self._cells[col][row - 1].visited is False:
                to_visit.append((col, row - 1))
            if row < self._num_rows - 1 and self._cells[col][row + 1].visited is False:
                to_visit.append((col, row + 1))
            
            if len(to_visit) == 0:
                self._draw_cell(i=row, j=col)
                return
            chosen_destination = random.randrange(0, len(to_visit))
            visit = to_visit.pop(chosen_destination)
            if visit[0] == col - 1:
                self._cells[col][row].has_left_wall = False
                self._cells[col - 1][row].has_right_wall = False
            if visit[0] == col + 1:
                self._cells[col][row].has_right_wall = False
                self._cells[col + 1][row].has_left_wall = False
            if visit[1] == row - 1:
                self._cells[col][row].has_top_wall = False
                self._cells[col][row - 1].has_bottom_wall = False
            if visit[1] == row + 1:
                self._cells[col][row].has_bottom_wall = False
                self._cells[col][row + 1].has_top_wall = False
            self._break_walls_r(visit[0], visit[1])
    
    def _reset_cells_visited(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row].visited = False

    def _solve_r(self, col, row):
        self._animate()
        cur_cell = self._cells[col][row] 
        cur_cell.visited = True
        if col == self._num_cols - 1 and row == self._num_rows - 1:
            return True
        if col > 0 and self._cells[col - 1][row].visited is False and cur_cell.has_left_wall == False:
            cur_cell.draw_move(self._cells[col - 1][row])
            if self._solve_r(col - 1, row) == True:
                return True
            else:
                cur_cell.draw_move(self._cells[col - 1][row], undo=True)
        if col < self._num_cols - 1 and self._cells[col + 1][row].visited is False and cur_cell.has_right_wall == False:
            cur_cell.draw_move(self._cells[col + 1][row])
            if self._solve_r(col + 1, row) == True:
                return True
            else:
                cur_cell.draw_move(self._cells[col + 1][row], undo=True)
        if row > 0 and self._cells[col][row - 1].visited is False and cur_cell.has_top_wall == False:
            cur_cell.draw_move(self._cells[col][row - 1])
            if self._solve_r(col, row - 1) == True:
                return True
            else:
                cur_cell.draw_move(self._cells[col][row - 1], undo=True)
        if row < self._num_rows - 1 and self._cells[col][row + 1].visited is False and cur_cell.has_bottom_wall == False:
            cur_cell.draw_move(self._cells[col][row + 1])
            if self._solve_r(col, row + 1) == True:
                return True
            else:
                cur_cell.draw_move(self._cells[col][row + 1], undo=True)

        return False
    
    def solve(self):
        return self._solve_r(0, 0)
            
