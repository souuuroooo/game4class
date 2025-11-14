#pause.py
import pygame
import os
import g_var
from cogs.ui_elements import TextButton

class Pause:
    def __init__(self):
        self.lable = pygame.font.SysFont("Microsoft JhengHei", 60)

        self.text = TextButton("Paused P=Resume",self.lable,(640,160))

        self.fishes = []
        for i in range(9):
            fish = pygame.image.load(os.path.join("cogs","fish_spin", f"{i}.png")).convert_alpha()
            fish_small = pygame.transform.scale(fish, (300, 300))
            self.fishes.append(fish_small)
        
        self.current_frame = 0
        self.frame_delay = 7
        self.counter = 0

  
    def update(self, events,screen):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                            return "game"

            if self.text.is_clicked(event):
                return "game"

        if self.current_frame==8:
            self.current_frame=0
        self.counter += 1
        if self.counter >= self.frame_delay:
            self.counter = 0
            self.current_frame = (self.current_frame + 1) 

            
        return "pause"

    def draw(self, screen):
        screen.fill((30, 30, 30))
        screen.blit(self.fishes[self.current_frame], (470, 300)) 
        self.text.update()
        self.text.draw(screen)