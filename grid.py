import numpy as np


class grid(object):

    def __init__(self, screen_x, screen_y, x, y, on=0.1, off=0.9, scale=2, margin=2):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.x = x
        self.y = y
        self.scale = scale
        self.margin = margin
        self.random_grid(on, off)

    def random_grid(self, on, off):
        self.grid = np.random.choice([0, 255], self.x * self.y, p=[off, on]).reshape(self.y, self.x)

    def add_glider(self, i, j):
        glider = np.array([[0, 0, 255], [255, 0, 255], [0, 255, 255]])
        self.grid[i:i+3, j:j+3] = glider

    def total_surrounding(self, i, j):
        total = self.grid[i, (j+1) % self.x] + \
                self.grid[i, (j-1) % self.x] + \
                self.grid[(i-1) % self.y, j] + \
                self.grid[(i+1) % self.y, j] + \
                self.grid[(i-1) % self.y, (j+1) % self.x] + \
                self.grid[(i-1) % self.y, (j-1) % self.x] + \
                self.grid[(i+1) % self.y, (j+1) % self.x] + \
                self.grid[(i+1) % self.y, (j-1) % self.x]
        return total / 255

    def render_this(self, i, j):
        if True if self.grid[i, j] == 255 else False:
            self.on_list.append((j * self.scale) + (self.screen_x / 2) - (self.x * self.scale / 2))
            self.on_list.append((i * self.scale) + (self.screen_y / 2) - (self.y * self.scale / 2))

            self.on_list.append((j * self.scale) + (self.screen_x / 2) - (self.x * self.scale / 2) + self.margin - self.scale)
            self.on_list.append((i * self.scale) + (self.screen_y / 2) - (self.y * self.scale / 2))

            self.on_list.append((j * self.scale) + (self.screen_x / 2) - (self.x * self.scale / 2) + self.margin - self.scale)
            self.on_list.append((i * self.scale) + (self.screen_y / 2) - (self.y * self.scale / 2) + self.margin - self.scale)

            self.on_list.append((j * self.scale) + (self.screen_x / 2) - (self.x * self.scale / 2))
            self.on_list.append((i * self.scale) + (self.screen_y / 2) - (self.y * self.scale / 2) + self.margin - self.scale)

    def apply_rules(self, i, j):
        self.render_this(i, j)
        total = self.total_surrounding(i, j)
        if (total < 2) or (total > 3):
            self.buffer_grid[i, j] = 0
        elif total == 3:
            self.buffer_grid[i, j] = 255

    def update(self, pause):
        self.buffer_grid = self.grid.copy()
        self.on_list = []
        if pause is False:
            for i in range(self.y):
                for j in range(self.x):
                    self.apply_rules(i, j)
        else:
            for i in range(self.y):
                for j in range(self.x):
                    self.render_this(i, j)
        self.grid[:] = self.buffer_grid[:]

    def turn_on(self, i, j):
        self.grid[i, j] = 255

    def turn_off(self, i, j):
        self.grid[i, j] = 0

    def on_at(self, i, j):
        return True if self.grid[i, j] == 255 else False
