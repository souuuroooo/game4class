import pygame
import os


wide = 1280

class Credits:

    def __init__(self):
        
        self.lable1 = pygame.font.SysFont("Microsoft JhengHei", 60)
        
        self.text=self.lable1.render("美術總監:google search,krita",True,"red")
        self.text2=self.lable1.render("程式總監:copilot,chatgpt,左手",True,"red")
        self.color=(30,30,30)
        self.flash_counter=0
        self.flash_speed=3
        
    def update(self, events,screen):
        for event in events:
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    return "start"
        self.flash_counter+=1
        if self.flash_counter < self.flash_speed :   
            self.color = (233,199,19)  
        elif self.flash_counter < self.flash_speed*2:
            self.color = (233,88,146)
        else:
            self.flash_counter=0

        self.text=self.lable1.render("美術總監:google search,krita",True,self.color)
        self.text2=self.lable1.render("程式總監:copilot,chatgpt,左手",True,self.color)

        return "credit"

    def draw(self, screen):
        screen.fill((30,30,30))
        screen.blit(self.text,(100,100))
        screen.blit(self.text2,(100,300))


