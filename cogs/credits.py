import pygame
import os


wide = 1280

class Credits:

    def __init__(self):
        
        self.lable1 = pygame.font.SysFont("Microsoft JhengHei", 60)
        
        self.text=self.lable1.render("美術總監:google search,krita",True,"red")
        self.text2=self.lable1.render("程式總監:copilot,chatgpt,左手",True,"red")
        
        
    def update(self, events,screen):
        

        return "credit"

    def draw(self, screen):
        
        screen.blit(self.text,(100,100))
        screen.blit(self.text2,(100,300))


