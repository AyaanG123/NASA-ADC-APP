from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import numpy as np
import random

app = Ursina()

# Window Title info
window.title = 'Astrovia'
window.fps_counter.enabled = True
max_frames = 60

window.fps_counter.max = 60




music = Audio(sound_file_name='assets/leonell-cassio-music.mp3', loop=True, autoplay=True, volume=10)
able_text = True

paused = False



def input(key):
    global paused
    if held_keys['space']:
        player.y += 800 * time.dt
    if held_keys['control']:
        player.y -= 800 * time.dt
    if key == 'p':
        paused = True
    if key == 'u':
        paused = False


class Planet(Entity):

    def __init__(self, x, y, z, scale, texture, name):
        super().__init__()
        self.model =load_model('earthModel.blend')
        self.collider = 'sphere'
        self.x = x
        self.y = y
        self.z = z
        self.scale = scale
        self.shader = lit_with_shadows_shader
        self.texture = texture
        self.name = name

        self.sun = False

    # Displays Name of the planet on the screen
    def input(self, key):
        def text_abler():
            global able_text
            able_text = True
        global paused, able_text
        if self.hovered and able_text:
            name_text = Text(text=self.name)
            able_text = False
            name_text.appear(speed=0.15)
            destroy(name_text, delay=3)
            invoke(text_abler, delay=3)

# Creates Sun


sun = Planet(0, 0, 0, 800, 'assets/8k_earth_daymap', "Earth")
sun.sun = True
# Makes sun exempt from the shader
sun.unlit = True

# light from sun
light1 = PointLight(shadows=True, color=color.red)



Sky(texture="assets/space")

player = FirstPersonController(position=(0, 3500, 0), gravity=0, speed=400)

app.run()