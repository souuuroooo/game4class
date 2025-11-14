#choose.py
import pygame
import os
import g_var
os.chdir(r"C:\Users\User\Desktop\game4class\cogs") 
          
class choose_char_2:
    def word_and_box(self, word, pos_x, pos_y,init_color=(30,30,30)):
        # 產生文字
        what_text = self.lable1.render(word, True, "white")
        text_center = what_text.get_rect(center=(pos_x, pos_y))

        # 建立比文字稍大的方框
        box_rect = pygame.Rect(0, 0, 200, 100) #固定200*100
        box_rect.center = (pos_x, pos_y)

        return what_text, text_center, box_rect ,init_color
        
    def __init__(self):
        self.lable1 = pygame.font.SysFont("Microsoft JhengHei", 40)
        self.lable2 = pygame.font.SysFont("Microsoft JhengHei", 60)

        self.pika_text, self.pika_text_center, self.pika_box ,self.pika_box_color = self.word_and_box("鼻孔獸", 640, 260)
        self.pika_click=False
        self.pika_use_hover=True
        self.pika_is_hover=False
        self.pika_border_color = (30,30,30)

        self.gob_text, self.gob_text_center, self.gob_box ,self.gob_box_color = self.word_and_box("哥布林", 340, 260)
        self.gob_click=False
        self.gob_use_hover=True
        self.gob_is_hover=False
        self.gob_border_color = (30,30,30)

        self.cat_text, self.cat_text_center, self.cat_box ,self.cat_box_color = self.word_and_box("貓", 940, 260)
        self.cat_click=False
        self.cat_use_hover=True
        self.cat_is_hover=False
        self.cat_border_color=(30,30,30)

        self.beach_text, self.beach_text_center, self.beach_box ,self.beach_box_color = self.word_and_box("beach", 640, 410)
        self.beach_click=False
        self.beach_use_hover=True
        self.beach_is_hover=False
        self.beach_border_color = (30,30,30)

        self.forest_text, self.forest_text_center, self.forest_box ,self.forest_box_color = self.word_and_box("forest", 340, 410)
        self.forest_click=False
        self.forest_use_hover=True
        self.forest_is_hover=False
        self.forest_border_color = (30,30,30)

        self.catbg_text, self.catbg_text_center, self.catbg_box ,self.catbg_box_color = self.word_and_box("cat_bg", 940, 410)
        self.catbg_click=False
        self.catbg_use_hover=True
        self.catbg_is_hover=False
        self.catbg_border_color = (30,30,30)

        self.go_text, self.go_text_center, self.go_box ,self.go_box_color = self.word_and_box("go", 640, 560)
        self.go_click=False
        self.go_is_hover=False
        self.go_border_color = (30,30,30)

        # self.get_text=self.lable1.render(f"{g_var.get_char}",True,"white")

        
        self.flash_counter = 0
        self.flash_speed = 5

        self.press_count=0
        

    def init_my_self(self):
        g_var.get_char="white"
        self.pika_click=False
        self.pika_box_color=(30,30,30)
        self.gob_click=False
        self.gob_box_color=(30,30,30)
        self.cat_click=False
        self.cat_box_color=(30,30,30)
        self.beach_click=False
        self.beach_box_color=(30,30,30)
        self.forest_click=False
        self.forest_box_color=(30,30,30)
        self.catbg_click=False
        self.catbg_box_color=(30,30,30)
        self.go_click=False
        self.go_box_color=(30,30,30)    

    def update(self, events, screen):
        #init
        if g_var.init_choose==True: 
            self.init_my_self()
            g_var.init_choose=False
        
        #hover #pika
        mouse_pos = pygame.mouse.get_pos()
        if self.pika_use_hover==True:
            if self.pika_box.collidepoint(mouse_pos):
                self.pika_box_color=(100,100,100)
                self.pika_is_hover=True
            else:
                self.pika_box_color=(30,30,30)
                self.pika_is_hover=False       
        #gob
        if self.gob_use_hover==True:
            if self.gob_box.collidepoint(mouse_pos):
                self.gob_box_color=(100,100,100)
                self.gob_is_hover=True
            else:
                self.gob_box_color=(30,30,30)
                self.gob_is_hover=False
        #cat
        if self.cat_use_hover==True:
            if self.cat_box.collidepoint(mouse_pos):
                self.cat_box_color=(100,100,100)
                self.cat_is_hover=True
            else:
                self.cat_box_color=(30,30,30)
                self.cat_is_hover=False
        #beach
        if self.beach_use_hover==True:
            if self.beach_box.collidepoint(mouse_pos):
                self.beach_box_color=(100,100,100)
                self.beach_is_hover=True
            else:
                self.beach_box_color=(30,30,30)
                self.beach_is_hover=False
        #forest
        if self.forest_use_hover==True:
            if self.forest_box.collidepoint(mouse_pos):
                self.forest_box_color=(100,100,100)
                self.forest_is_hover=True
            else:
                self.forest_box_color=(30,30,30)
                self.forest_is_hover=False

        #cat
        if self.catbg_use_hover==True:
            if self.catbg_box.collidepoint(mouse_pos):
                self.catbg_box_color=(100,100,100)
                self.catbg_is_hover=True
            else:
                self.catbg_box_color=(30,30,30)
                self.catbg_is_hover=False
        
        #go
        if self.go_box.collidepoint(mouse_pos):
            self.go_box_color=(100,100,100)
            self.go_is_hover=True
        else:
            self.go_box_color=(30,30,30)
            self.go_is_hover=False

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    return "start"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #pika的
                if self.pika_box.collidepoint(event.pos): #pika button
                    if self.pika_click==False: #選pika
                        self.pika_box_color=(100,100,100)
                        g_var.get_char="pika"
                        self.pika_use_hover=False
                        self.pika_border_color = (30,30,30)
                        self.pika_click=True
                    elif self.pika_click==True: #取消pika
                        self.pika_box_color=(30,30,30)
                        g_var.get_char="white"
                        self.pika_use_hover=True
                        self.pika_click=False
                #pika的end
                #gob的
                if self.gob_box.collidepoint(event.pos): #gob button
                    if self.gob_click==False: #選gob
                        self.gob_box_color=(100,100,100)
                        g_var.get_char="gob"
                        self.gob_use_hover=False
                        self.gob_border_color = (30,30,30)
                        self.gob_click=True
                    elif self.gob_click==True: #取消gob
                        self.gob_box_color=(30,30,30)
                        g_var.get_char="white"
                        self.gob_use_hover=True
                        self.gob_click=False
                #gob的end
                #cat的
                if self.cat_box.collidepoint(event.pos): #cat button
                    if self.cat_click==False: #選cat
                        self.cat_box_color=(100,100,100)
                        g_var.get_char="cat"
                        self.cat_use_hover=False
                        self.cat_border_color = (30,30,30)
                        self.cat_click=True
                    elif self.cat_click==True: #取消cat
                        self.cat_box_color=(30,30,30)
                        g_var.get_char="white"
                        self.cat_use_hover=True
                        self.cat_click=False
                #cat的end
                #beach的
                if self.beach_box.collidepoint(event.pos): #beach button
                    if self.beach_click==False: #選beach
                        self.beach_box_color=(100,100,100)
                        g_var.get_bg="beach"
                        self.beach_use_hover=False
                        self.beach_border_color = (30,30,30)
                        self.beach_click=True
                    elif self.beach_click==True: #取消beach
                        self.beach_box_color=(30,30,30)
                        g_var.get_bg="beach"
                        self.beach_use_hover=True
                        self.beach_click=False
                #beach的end
                #forest的
                if self.forest_box.collidepoint(event.pos): #forest button
                    if self.forest_click==False: #選forest
                        self.forest_box_color=(100,100,100)
                        g_var.get_bg="forest"
                        self.forest_use_hover=False
                        self.forest_border_color = (30,30,30)
                        self.forest_click=True
                    elif self.forest_click==True: #取消forest
                        self.forest_box_color=(30,30,30)
                        g_var.get_bg="forest"
                        self.forest_use_hover=True
                        self.forest_click=False
                #forest的end
                #cat的
                if self.catbg_box.collidepoint(event.pos): #cat button
                    if self.catbg_click==False: #選cat
                        self.catbg_box_color=(100,100,100)
                        g_var.get_bg="cat"
                        self.catbg_use_hover=False
                        self.catbg_border_color = (30,30,30)
                        self.catbg_click=True
                    elif self.catbg_click==True: #取消cat
                        self.catbg_box_color=(30,30,30)
                        g_var.get_bg="cat"
                        self.catbg_use_hover=True
                        self.catbg_click=False
                #cat的end
                
                if self.go_box.collidepoint(event.pos):
                    return "game"
        
        self.flash_counter = (self.flash_counter + 1) % (self.flash_speed*2)
                    

        return "char_2"

    def draw(self, screen):
        screen.fill((30, 30, 30))
        
        #pika use hover
        if self.pika_use_hover==True:
            if self.pika_is_hover:
                if self.flash_counter < self.flash_speed:   
                    self.pika_border_color = (233,199,19)  
                else:
                    self.pika_border_color = (233,88,146)
            else:
                self.pika_border_color = (30,30,30)
        
        #gob use hover
        if self.gob_use_hover==True:
            if self.gob_is_hover:
                if self.flash_counter < self.flash_speed:   
                    self.gob_border_color = (233,199,19)  
                else:
                    self.gob_border_color = (233,88,146)
            else:
                self.gob_border_color = (30,30,30)
        
        #cat use hover
        if self.cat_use_hover==True:
            if self.cat_is_hover:
                if self.flash_counter < self.flash_speed:   
                    self.cat_border_color = (233,199,19)  
                else:
                    self.cat_border_color = (233,88,146)
            else:
                self.cat_border_color = (30,30,30)
        
        #beach use hover
        if self.beach_use_hover==True:
            if self.beach_is_hover:
                if self.flash_counter < self.flash_speed:   
                    self.beach_border_color = (233,199,19)  
                else:
                    self.beach_border_color = (233,88,146)
            else:
                self.beach_border_color = (30,30,30)
        
        #forest use hover
        if self.forest_use_hover==True:
            if self.forest_is_hover:
                if self.flash_counter < self.flash_speed:   
                    self.forest_border_color = (233,199,19)  
                else:
                    self.forest_border_color = (233,88,146)
            else:
                self.forest_border_color = (30,30,30)
        
        #cat use hover
        if self.catbg_use_hover==True:
            if self.catbg_is_hover:
                if self.flash_counter < self.flash_speed:   
                    self.catbg_border_color = (233,199,19)  
                else:
                    self.catbg_border_color = (233,88,146)
            else:
                self.catbg_border_color = (30,30,30)

        #go use hover
        if self.go_is_hover:
            if self.flash_counter < self.flash_speed:   
                self.go_border_color = (233,199,19)  
            else:
                self.go_border_color = (233,88,146)
        else:
            self.go_border_color = (30,30,30)
        

        pygame.draw.rect(screen, self.pika_box_color, self.pika_box,border_radius=10) #pika button
        pygame.draw.rect(screen, self.pika_border_color, self.pika_box, width=6, border_radius=10) #閃
        pygame.draw.rect(screen, self.gob_box_color, self.gob_box,border_radius=10) #gob button
        pygame.draw.rect(screen, self.gob_border_color, self.gob_box, width=6, border_radius=10) #閃
        pygame.draw.rect(screen, self.cat_box_color, self.cat_box,border_radius=10) #cat button
        pygame.draw.rect(screen, self.cat_border_color, self.cat_box, width=6, border_radius=10) #閃
        pygame.draw.rect(screen, self.beach_box_color, self.beach_box,border_radius=10) #beach button
        pygame.draw.rect(screen, self.beach_border_color, self.beach_box, width=6, border_radius=10) #閃
        pygame.draw.rect(screen, self.forest_box_color, self.forest_box,border_radius=10) #forest button
        pygame.draw.rect(screen, self.forest_border_color, self.forest_box, width=6, border_radius=10) #閃
        pygame.draw.rect(screen, self.catbg_box_color, self.catbg_box,border_radius=10) #cat button
        pygame.draw.rect(screen, self.catbg_border_color, self.catbg_box, width=6, border_radius=10) #閃
        pygame.draw.rect(screen,self.go_box_color,self.go_box,border_radius=10)
        pygame.draw.rect(screen, self.go_border_color, self.go_box, width=6, border_radius=10) #閃

        screen.blit(self.pika_text, self.pika_text_center) #pika word
        screen.blit(self.gob_text, self.gob_text_center) #gob word
        screen.blit(self.cat_text, self.cat_text_center) #cat word
        screen.blit(self.beach_text, self.beach_text_center) #beach word
        screen.blit(self.forest_text, self.forest_text_center) #forest word
        screen.blit(self.catbg_text, self.catbg_text_center) #cat word
        screen.blit(self.go_text,self.go_text_center)

        get_text=self.lable1.render(f"{g_var.get_char}",True,"white")
        screen.blit(get_text,(100,100))
        get_text=self.lable1.render(f"{g_var.get_char_2}",True,"white")
        screen.blit(get_text,(100,250))
        





