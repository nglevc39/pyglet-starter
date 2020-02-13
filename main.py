import pyglet # import the library
win = pyglet.window.Window() # create the window
keys = pyglet.window.key.KeyStateHandler()
# Load the image
img = pyglet.image.load('assets/0/sliced/idle-1.png')
spr = pyglet.sprite.Sprite(img, x = 300, y = 250)

# spr = pyglet.sprite.Sprite(img, x=50, y=50)

# Start the event loop
keys = pyglet.window.key.KeyStateHandler()

def update(dt):
    win.push_handlers(keys)             # update the keys object
    if keys[pyglet.window.key.LEFT]: 
        spr.x -= 2 
    if keys[pyglet.window.key.RIGHT]: 
        spr.x += 2 
    if keys[pyglet.window.key.DOWN]: 
        spr.y -= 2  
    if keys[pyglet.window.key.UP]: 
        spr.y += 2                             # change spr.x by -1


@win.event
def on_draw():
  win.clear()
  # img.blit(200, 100)
  spr.draw()

pyglet.clock.schedule(update)
pyglet.app.run()