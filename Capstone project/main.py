import pgzrun

WIDTH = 600
HEIGHT = 800

TITLE = "CROSSY ROAD"

chicken = Actor("chicken")
bug = Actor("bug")
finish = Actor("finish")

chicken.pos = (275, 740)
finish.pos = (300,25)

speed = 5

enemies = []

score = 0
direction = 1

chicken.dead = False

def on_key_down(key):
    if chicken.dead == False:
        if key == key.SPACE:
            chicken.y = chicken.y - 20

for i in range(6):
    enemies.append (Actor("bug"))
    

def update():
    pass

def draw():
    screen.clear()
    screen.fill("green")

    chicken.draw()
    finish.draw()


pgzrun.go()