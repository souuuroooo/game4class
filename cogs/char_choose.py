import pygame
import os
from cogs.ui_elements import TextButton
from cogs.ui_elements import TextButtonToggle
import g_var

          
class choose_char:
    def __init__(self):
        self.lable1 = pygame.font.SysFont("Microsoft JhengHei", 40)
        self.lable2 = pygame.font.SysFont("Microsoft JhengHei", 60)
        
        self.pika = TextButtonToggle("鼻孔獸", self.lable1, (640, 360))
        self.blue = TextButtonToggle("cat", self.lable1, (300, 360))
        self.yellow = TextButtonToggle("哥布林", self.lable1, (980, 360))
        self.beach = TextButton("beach", self.lable1, (300, 460))
        self.forest = TextButton("forest", self.lable1, (640, 460))
        self.cat = TextButton("cat bg", self.lable1, (980, 460))

        self.text_choose = self.lable2.render("選球再選場景 球預設:白", True, (200,200,200))
        self.text_choose_rect = self.text_choose.get_rect(center=(640, 200))

        # 收集所有 toggle 按鈕，方便管理
        self.toggle_buttons = [self.pika, self.blue, self.yellow]

    def reset_toggles(self):
        """重置所有顏色按鈕狀態"""
        for btn in self.toggle_buttons:
            btn.toggled = False
        # g_var.get = "white"  # 也可以順便把選的顏色清空

    def update(self, events,screen):
        if g_var.restart_choose==True: #restart_choose是從game 的esc來的
            g_var.get = "white"
            g_var.restart_choose=False

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            
            if self.pika.is_clicked(event):
                self.reset_toggles()
                g_var.get_char = "pika" 
                self.pika.is_clicked(event)==True                            
            if self.blue.is_clicked(event):
                self.reset_toggles()
                g_var.get_char = "cat"
                self.blue.is_clicked(event)==True
            if self.yellow.is_clicked(event):
                self.reset_toggles()
                g_var.get_char = "gob"
                self.yellow.is_clicked(event)==True

            if self.beach.is_clicked(event):
                self.reset_toggles()
                g_var.get_bg="beach"               
                return "game"
            if self.forest.is_clicked(event):
                self.reset_toggles()
                g_var.get_bg="forest"  
                return "game"               
            if self.cat.is_clicked(event):
                self.reset_toggles()
                g_var.get_bg="cat"    
                return "game" 
  
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.reset_toggles()   # <--- 這裡加上重置
                    g_var.get="white"
                    return "start"

        return "char"
    def draw(self, screen):
        screen.fill((30, 30, 30)) 
        screen.blit(self.text_choose, self.text_choose_rect) 
        
        self.pika.update()
        self.blue.update()
        self.yellow.update()
        self.beach.update()
        self.forest.update()
        self.cat.update()
        
        self.pika.draw(screen)
        self.blue.draw(screen)
        self.yellow.draw(screen)
        self.beach.draw(screen)
        self.forest.draw(screen)
        self.cat.draw(screen)


