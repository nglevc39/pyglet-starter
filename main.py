import pyglet # import the library
win= pyglet.window.Window() # create the window

# Create a sprite
img= pyglet.image.load('Nature.jpg')

def update(dt):
  pass

# Start the event loop
@win.event
def on_draw():
    win.clear()
    img.blit(100, 150)

pyglet.clock.schedule(update) 
pyglet.app.run()
