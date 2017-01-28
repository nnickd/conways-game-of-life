import numpy as np


class grid(object):

    def __init__(self, x, y, on=0.1, off=0.9):
        self.x = x
        self.y = y
        self.random_grid(on, off)
        self.on_list = []

    def random_grid(self, on, off):
        self.grid = np.random.choice([0, 255], self.x * self.y, p=[off, on]).reshape(self.y, self.x)

    def add_glider(self, i, j):
        glider = np.array([[0, 0, 255], [255, 0, 255], [0, 255, 255]])
        self.grid[i:i+3, j:j+3] = glider

    def on_at(self, i, j):
        return True if self.grid[i, j] == 255 else False

    def bounds(self, i, j, direction):
        if direction == "right":
            return self.grid[i, (j+1) % self.x]
        elif direction == "left":
            return self.grid[i, (j-1) % self.x]
        elif direction == "up":
            return self.grid[(i-1) % self.y, j]
        elif direction == "down":
            return self.grid[(i+1) % self.y, j]
        elif direction == "up-right":
            return self.grid[(i-1) % self.y, (j+1) % self.x]
        elif direction == "up-left":
            return self.grid[(i-1) % self.y, (j-1) % self.x]
        elif direction == "down-right":
            return self.grid[(i+1) % self.y, (j+1) % self.x]
        elif direction == "down-left":
            return self.grid[(i+1) % self.y, (j-1) % self.x]

    def total_surrounding(self, i, j):
        total = self.bounds(i, j, 'right')
        total += self.bounds(i, j, 'left')
        total += self.bounds(i, j, 'up')
        total += self.bounds(i, j, 'down')
        total += self.bounds(i, j, 'up-right')
        total += self.bounds(i, j, 'up-left')
        total += self.bounds(i, j, 'down-right')
        total += self.bounds(i, j, 'down-left')
        return total / 255

    def apply_rules(self, i, j, buffer_grid):
        if self.on_at(i, j):
            # self.on_list.append((i+600, j+600))
            self.on_list.append(i+600)
            self.on_list.append(j+600)
        total = self.total_surrounding(i, j)
        if (total < 2) or (total > 3):
            buffer_grid[i, j] = 0
        elif total == 3:
            buffer_grid[i, j] = 255

    def update(self):
        self.on_list = []
        buffer_grid = self.grid.copy()
        for i in range(self.y):
            for j in range(self.x):
                self.apply_rules(i, j, buffer_grid)
        self.grid[:] = buffer_grid[:]
