#main.py
import pygame
from cogs.start_menu import StartMenu
from cogs.game_scene import GameScene
from cogs.pause import Pause
from cogs.skills import Skill
from cogs.p1_get_char import p1_choose
from cogs.p2_get_char import p2_choose
from cogs.select_bg import select_bg
from cogs.select_point import point
from cogs.win import victory

from cogs.credits import Credits

import g_var

pygame.init()
# pygame.mixer.init()
# music=pygame.mixer.Sound("Angel_boring.ogg")
# music.set_volume(0.3)
# music.play(loops=-1)
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game4class")
clock = pygame.time.Clock()

# 場景 #9/11A部分
scenes = { 
    "start": StartMenu(),
    "game":GameScene(WIDTH,HEIGHT),
    "p1":p1_choose(),
    "p2":p2_choose(),
    "bg":select_bg(),
    "pause":Pause(),
    "skill":Skill(),
    "credit":Credits(),
    "point":point(),
    "win":victory(),
}
active_scene = "start"

running = True
while running:
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # 更新 & 場景切換
    
    new_scene = scenes[active_scene].update(events,screen)
    if new_scene != active_scene:
        active_scene = new_scene

    # 繪製
    scenes[active_scene].draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit() 