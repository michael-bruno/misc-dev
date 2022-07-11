'''
File:   game-of-life.py
Author: Michael Bruno

GAME OF LIFE RULES
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
'''

import matplotlib.pyplot as plt

import random
import numpy
import os


class Enum:
    Empty = 0
    Occupied = 1


class Cell:
    def __init__(self, x, y, state):
        self.state = state
        self.x = x
        self.y = y


class Grid:

    def __init__(self, height=50, width=50):
        self.height = height
        self.width = width
        self.grid = []
        self.iters = 0
            
    def _init(self):

        for i in range(self.height):

            row = []
            for j in range(self.width):
                new_cell = None
                if random.randrange(0, 4) == 1:
                    new_cell = Cell(j, i, Enum.Occupied)
                else:
                    new_cell = Cell(j, i, Enum.Empty)
                row.append(new_cell)

            self.grid.append(row)

    def display(self):

        grid = [[c.state for c in row] for row in self.grid]

        H = numpy.array(grid)

        plt.gca().axes.get_yaxis().set_visible(False)
        plt.gca().axes.get_xaxis().set_visible(False)

        plt.imshow(H)
        
        plt.pause(1e-17)
        plt.cla()

        os.system('cls')
        print(f'Generation: {self.iters}')

    def is_alive(self):
        grid = [[c.state for c in row] for row in self.grid]

        return sum(sum(grid,[])) > 0

    def count_neighbors(self, cell):
        'right->left & top->bottom'

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),(0, 1), (1, -1), (1, 0), (1, 1)]

        neighbors = 0
        for dy, dx in directions:
            ny, nx = cell.y + dy, cell.x + dx

            try:
                if self.grid[ny][nx].state:
                    neighbors += 1
            except IndexError:
                pass

        return neighbors

    def tick(self):
        new_grid = []

        for i, row in enumerate(self.grid):
            new_row = []
            for j, cell in enumerate(row):
                neighbors = self.count_neighbors(cell)
                new_cell = cell

                if cell.state:
                    if neighbors < 2:
                        new_cell = Cell(j, i, Enum.Empty)

                    elif neighbors in [2, 3]:
                        pass

                    elif neighbors > 3:
                        new_cell = Cell(j, i, Enum.Empty)

                else:
                    if neighbors == 3:
                        new_cell = Cell(j, i, Enum.Occupied)

                new_row.append(new_cell)
            new_grid.append(new_row)

        return new_grid


    def run(self):
        plt.show(block=False)
        plt.suptitle('game-of-life')

        self._init()

        while self.is_alive():
            self.display()
            self.grid = self.tick()
            self.iters += 1


if __name__ == '__main__':
    grid = Grid(100, 100)
    grid.run()
