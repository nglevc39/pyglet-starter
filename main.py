import pyglet # import the library
win = pyglet.window.Window() # create the window
keys = pyglet.window.key.KeyStateHandler()
# Load the image



img= pyglet.image.load('assets/gfx/knight.gif')
smol_img = img.get_region(x=30, y=30, width=16, height=16)
spr = pyglet.sprite.Sprite(smol_img, x = 300, y = 250)

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
        spr.y += 2  


@win.event
def on_draw():
  win.clear()
  # img.blit(200, 100)
  spr.draw()

if spr.x ? 800:
    hp -= 1
pyglet.clock.schedule(update)
pyglet.app.run()