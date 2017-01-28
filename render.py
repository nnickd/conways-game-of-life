import pyglet
import numpy as np
from grid import grid
from random import random


class render(object):
    window = pyglet.window.Window(fullscreen=True)
    vertex_list = None
    n = 0.5


    def __init__(self):
        self.grid = grid(100, 100, 0.4, 0.6)
        self.grid.update()

        self.amount = len(self.grid.on_list) // 2
        colors = [(255, 0, 0) for i in range(self.amount)]
        print(self.amount)
        print(len(colors))

        render.vertex_list = pyglet.graphics.vertex_list(self.amount, 'v2f/stream', 'c3B/static')
        render.vertex_list.vertices = self.grid.on_list
        render.vertex_list.colors = np.array(colors).flatten()

        pyglet.clock.schedule_interval(self.update, 1/30)
        pyglet.app.run()

    def update(self, dt):
        self.grid.update()
        print(self.grid.on_list)
        render.vertex_list = pyglet.graphics.vertex_list(len(self.grid.on_list) // 2, 'v2f/stream', 'c3B/static')
        render.vertex_list.vertices = self.grid.on_list
        render.vertex_list.colors = np.array([(255, 0, 0) for i in range(len(self.grid.on_list) // 2)]).flatten()

    @window.event
    def on_draw():
        render.window.clear()
        render.vertex_list.draw(pyglet.gl.GL_POINTS)


r = render()
