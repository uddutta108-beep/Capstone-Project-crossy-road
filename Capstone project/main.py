import pgzrun, random

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

for y in range(10):
    enemies.append (Actor("bug"))

    enemies[-1].y = 100 + 50 * y

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
    for enemy in enemies:
        if (enemies[-1].x > WIDTH or enemies[0].x < 0):

            direction = direction*-1

        
        enemy.x += 5*direction
        direction = random.randint(1,3)

# create different actors for each bug


pgzrun.go()