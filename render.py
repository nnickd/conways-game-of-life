import pyglet
import numpy as np
from grid import grid
from random import random
from pyglet.window import mouse, key
import time


class render(object):
    window = pyglet.window.Window(fullscreen=True)
    vertex_list = None

    i = 0
    t = time.time()
    m = t

    def __init__(self):
        self.grid = grid(1920//10, 1080//10, 0.5, 0.5, 3, 3)
        self.update(1)

        pyglet.clock.schedule_interval(self.update, 1/30)
        pyglet.app.run()

    def update(self, dt):
        self.grid.update()
        render.vertex_list = pyglet.graphics.vertex_list(len(self.grid.on_list) // 2, 'v2f/stream', 'c3B/static')
        render.vertex_list.vertices = self.grid.on_list
        render.vertex_list.colors = np.array([(0, 255, int(random() * 255)) for i in range(len(self.grid.on_list) // 2)]).flatten()

    @window.event
    def on_draw():
        render.window.clear()
        render.vertex_list.draw(pyglet.gl.GL_POINTS)
        render.i += 1
        if render.i % 10 == 0:
            print(render.i, time.time() - render.m)
            render.m = time.time()
            if render.i == 100:
                print(render.i, time.time() - render.t)
                pyglet.app.exit()

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.DOWN:
            print(render.i)
            print(time.time() - render.t)
            pyglet.app.exit()


r = render()
