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

for y in range(12):
    enemies.append (Actor("bug"))

    enemies[-1].y = 80 + 50 * y

def draw():
    screen.clear()
    screen.fill("green")

    if chicken.dead == False:
        chicken.draw()
    
    finish.draw()

    for enemy in enemies:
        enemy.draw()

def update():
    global direction, enemies

    if (enemies[-1].x < WIDTH-80 or enemies[0].x > 80):

        direction = direction*-1

    for enemy in enemies:
        enemy.x += 5*direction



pgzrun.go()