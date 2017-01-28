import pyglet
import numpy as np
from grid import grid
from random import random
from pyglet.window import mouse, key
import time


class render(object):
    x = 100
    y = 100
    window = pyglet.window.Window(x, y)
    # window = pyglet.window.Window(fullscreen=True)
    vertex_list = None
    grid = grid(screen_x=x, screen_y=y, x=50, y=50, on=0.5, off=0.5, scale=2, margin=0)

    i = 0
    t = time.time()
    m = t

    def __init__(self):
        self.update(1)

        pyglet.clock.schedule_interval(self.update, 1/30)
        pyglet.app.run()

    def update(self, dt):
        # t = time.time()

        render.grid.update()
        render.vertex_list = pyglet.graphics.vertex_list(len(render.grid.on_list) // 2, 'v2f/stream', 'c3B/static')
        render.vertex_list.vertices = render.grid.on_list
        render.vertex_list.colors = np.array([(0, 255, int(random() * 255)) for i in range(len(render.grid.on_list) // 2)]).flatten()

        # if render.i % 10 == 0:
        #     print(render.i, time.time() - render.t, render.i / (time.time() - render.t))
        #     print(len(render.grid.on_list) // 2, time.time() - t)

        render.i += 1

    @window.event
    def on_draw():
        render.window.clear()
        render.vertex_list.draw(pyglet.gl.GL_QUADS)

        # if render.i == 1000:
        #     print(render.i, time.time() - render.t, render.i / (time.time() - render.t))
        #     pyglet.app.exit()

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == key.DOWN:
            print(render.i, time.time() - render.m)
            print(time.time() - render.t)
            pyglet.app.exit()

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            j = (x + (render.grid.x * render.grid.scale // 2) - (render.x / 2)) // render.grid.scale + 1
            i = (y + (render.grid.y * render.grid.scale // 2) - (render.y / 2)) // render.grid.scale + 1
            render.grid.turn_on(i, j)

        if button == mouse.RIGHT:
            pass


r = render()
