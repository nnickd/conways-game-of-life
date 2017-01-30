import pyglet
import numpy as np
from grid import grid
from random import random
from pyglet.window import mouse, key
import time


class render(object):
    pause = False
    vertex_list = None
    grid = grid(x=30, y=30, on=0.5, off=0.5, scale=30, margin=1)
    window = pyglet.window.Window(grid.scaled_x, grid.scaled_y, resizable=True)
    screen_x = grid.scaled_x
    screen_y = grid.scaled_y

    i = 0
    t = time.time()
    m = t

    def __init__(self):
        self.update(1)

        pyglet.clock.schedule_interval(self.update, 1/30)
        pyglet.app.run()

    def update(self, dt):
        # t = time.time()

        render.grid.update(render.pause)
        render.vertex_list = pyglet.graphics.vertex_list(len(render.grid.on_list) // 2, 'v2f/stream', 'c3B/static')
        render.vertex_list.vertices = render.grid.on_list
        render.vertex_list.colors = np.array([(0, 255, int(random() * 255)) for i in range(len(render.grid.on_list) // 2)]).flatten()

        # if render.i % 10 == 0:
        #     print(render.i, time.time() - render.t, render.i / (time.time() - render.t))
        #     print(len(render.grid.on_list) // 2, time.time() - t)

        render.i += 1

    @window.event
    def on_resize(width, height):
        render.grid.screen_x = width
        render.grid.screen_y = height
        pass

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
        if symbol == key.RIGHT:
            render.grid.scale += 1
            render.window.set_size(render.grid.scaled_x, render.grid.scaled_y)
        if symbol == key.LEFT:
            render.grid.scale -= 1
            render.window.set_size(render.grid.scaled_x, render.grid.scaled_y)
        if symbol == key.UP:
            render.pause = not render.pause

    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT:
            j = (x + (render.grid.scaled_x // 2) - (render.grid.screen_x // 2)) // render.grid.scale + 1
            i = (y + (render.grid.scaled_y // 2) - (render.grid.screen_y // 2)) // render.grid.scale + 1
            render.grid.turn_on(i, j)

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            j = (x + (render.grid.scaled_x // 2) - (render.grid.screen_x // 2)) // render.grid.scale + 1
            i = (y + (render.grid.scaled_y // 2) - (render.grid.screen_y // 2)) // render.grid.scale + 1
            if render.grid.on_at(i, j):
                render.grid.turn_off(i, j)
            else:
                render.grid.turn_on(i, j)

        if button == mouse.RIGHT:
            render.grid.clear()
            render.pause = True


r = render()
