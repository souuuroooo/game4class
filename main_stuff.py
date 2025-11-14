#main.py
import pygame
from cogs.start_menu import StartMenu
from cogs.game_scene import GameScene
# from cogs.game_test import GameScene_test
# from cogs.char_choose import choose_char
from cogs.pause import Pause
from cogs.skills import Skill
# from cogs.choose import choose_chaar_2
from cogs.p1_get_char import p1_choose
from cogs.p2_get_char import p2_choose
from cogs.select_bg import select_bg

# from cogs.test_start import StartMenu_Test 

import g_var

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game4class")
clock = pygame.time.Clock()

# 場景 #9/11A部分
scenes = { 
    "start": StartMenu(),
    "game":GameScene(WIDTH,HEIGHT),
    # "test":GameScene_test(WIDTH,HEIGHT),
    # "char": choose_char(),
    # "char_2": choose_char_2(),
    "p1":p1_choose(),
    "p2":p2_choose(),
    "bg":select_bg(),
    "pause":Pause(),
    "skill":Skill(),

    # "start":StartMenu_Test()
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