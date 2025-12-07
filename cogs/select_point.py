#select_point.py
import pygame
import os
import g_var
from cogs.characters import Character
          
class point:
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

        self.pika_text, self.pika_text_center, self.pika_box ,self.pika_box_color = self.word_and_box("21分制", 640, 360)
        self.pika_click=False
        self.pika_use_hover=True
        self.pika_is_hover=False
        self.pika_border_color = (30,30,30)

        self.gob_text, self.gob_text_center, self.gob_box ,self.gob_box_color = self.word_and_box("14分制", 340, 360)
        self.gob_click=False
        self.gob_use_hover=True
        self.gob_is_hover=False
        self.gob_border_color = (30,30,30)

        self.cat_text, self.cat_text_center, self.cat_box ,self.cat_box_color = self.word_and_box("急速5分制", 940, 360)
        self.cat_click=False
        self.cat_use_hover=True
        self.cat_is_hover=False
        self.cat_border_color=(30,30,30)


        self.go_text, self.go_text_center, self.go_box ,self.go_box_color = self.word_and_box("go", 640, 560)
        self.go_click=False
        self.go_is_hover=False
        self.go_border_color = (30,30,30)

        
        self.flash_counter = 0
        self.flash_speed = 5

        

    def init_my_self(self):
        g_var.format="14"
        self.pika_click=False
        self.pika_box_color=(30,30,30)
        self.gob_click=False
        self.gob_box_color=(30,30,30)
        self.cat_click=False
        self.cat_box_color=(30,30,30)

        self.gob_use_hover=True
        self.cat_use_hover=True
        self.pika_use_hover=True
    
        self.go_click=False
        self.go_box_color=(30,30,30) 


    def update(self, events, screen):
        #init       
        if g_var.init_choose==True: 
            self.init_my_self()
            g_var.init_choose=False
        
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
                        g_var.point=21
                        self.pika_use_hover=False
                        self.pika_border_color = (30,30,30)
                        
                        self.gob_box_color=(30,30,30)
                        self.cat_box_color=(30,30,30)
                        self.cat_use_hover=True
                        self.gob_use_hover=True

                        self.gob_click=False
                        self.cat_click=False

                        self.show_pika=True
                        self.show_gob=False
                        self.show_cat=False

                        self.pika_click=True
                    elif self.pika_click==True: #取消pika
                        self.pika_box_color=(30,30,30)
                        g_var.point=14
                        self.pika_use_hover=True
                        self.pika_click=False

                        self.show_pika=False
                #pika的end
                #gob的
                if self.gob_box.collidepoint(event.pos): #gob button
                    if self.gob_click==False: #選gob
                        self.gob_box_color=(100,100,100)
                        g_var.point=14
                        self.gob_use_hover=False
                        self.gob_border_color = (30,30,30)
                        
                        self.pika_box_color=(30,30,30)
                        self.cat_box_color=(30,30,30)
                        self.cat_use_hover=True
                        self.pika_use_hover=True

                        self.pika_click=False
                        self.cat_click=False

                        self.show_pika=False
                        self.show_gob=True
                        self.show_cat=False

                        self.gob_click=True
                    elif self.gob_click==True: #取消gob
                        self.gob_box_color=(30,30,30)
                        g_var.point=14
                        self.gob_use_hover=True
                        self.gob_click=False
                        
                        self.show_gob=False
                #gob的end
                #cat的
                if self.cat_box.collidepoint(event.pos): #cat button
                    if self.cat_click==False: #選cat
                        self.cat_box_color=(100,100,100)
                        g_var.point=5
                        self.cat_use_hover=False
                        self.cat_border_color = (30,30,30)
                        
                        self.pika_box_color=(30,30,30)
                        self.gob_box_color=(30,30,30)
                        self.gob_use_hover=True
                        self.pika_use_hover=True

                        self.pika_click=False
                        self.gob_click=False

                        self.show_pika=False
                        self.show_gob=False
                        self.show_cat=True

                        self.cat_click=True
                    elif self.cat_click==True: #取消cat
                        self.cat_box_color=(30,30,30)
                        g_var.point=14
                        self.cat_use_hover=True
                        self.cat_click=False

                        self.show_cat=False
                #cat的end
                
                if self.go_box.collidepoint(event.pos):
                    g_var.init_choose=True
                    return "game"
      
        #hover 
        #pika
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
        
        #go
        if self.go_box.collidepoint(mouse_pos):
            self.go_box_color=(100,100,100)
            self.go_is_hover=True
        else:
            self.go_box_color=(30,30,30)
            self.go_is_hover=False
        
        self.flash_counter = (self.flash_counter + 1) % (self.flash_speed*2)

        return "point"

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
       
        pygame.draw.rect(screen,self.go_box_color,self.go_box,border_radius=10)
        pygame.draw.rect(screen, self.go_border_color, self.go_box, width=6, border_radius=10) #閃

        screen.blit(self.pika_text, self.pika_text_center) #pika word
        screen.blit(self.gob_text, self.gob_text_center) #gob word
        screen.blit(self.cat_text, self.cat_text_center) #cat word
       
        screen.blit(self.go_text,self.go_text_center)

        # get_text=self.lable1.render(f"{g_var.get_char}",True,"white")
        # screen.blit(get_text,(100,100))

        text=self.lable1.render("選賽制",True,"white")
        middle=text.get_rect(center=(640,150))
        screen.blit(text,middle)


        # self.pika.draw(screen,200,500)
        





# #p1_get_char
# import pygame
# import os
# import g_var
          
# class point:
#     def word_and_box(self, word, pos_x, pos_y,init_color=(30,30,30)):
#         # 產生文字
#         what_text = self.lable1.render(word, True, "white")
#         text_center = what_text.get_rect(center=(pos_x, pos_y))

#         # 建立比文字稍大的方框
#         box_rect = pygame.Rect(0, 0, 200, 100) #固定200*100
#         box_rect.center = (pos_x, pos_y)

#         return what_text, text_center, box_rect ,init_color
        
#     def __init__(self):
#         self.lable1 = pygame.font.SysFont("Microsoft JhengHei", 40)
#         self.lable2 = pygame.font.SysFont("Microsoft JhengHei", 60)

#         self.pika_text, self.pika_text_center, self.pika_box ,self.pika_box_color = self.word_and_box("21", 640, 360)
#         self.pika_click=False
#         self.pika_use_hover=True
#         self.pika_is_hover=False
#         self.pika_border_color = (30,30,30)

#         self.gob_text, self.gob_text_center, self.gob_box ,self.gob_box_color = self.word_and_box("14", 340, 360)
#         self.gob_click=False
#         self.gob_use_hover=True
#         self.gob_is_hover=False
#         self.gob_border_color = (30,30,30)

#         self.cat_text, self.cat_text_center, self.cat_box ,self.cat_box_color = self.word_and_box("5", 940, 360)
#         self.cat_click=False
#         self.cat_use_hover=True
#         self.cat_is_hover=False
#         self.cat_border_color=(30,30,30)


#         self.go_text, self.go_text_center, self.go_box ,self.go_box_color = self.word_and_box("go", 640, 560)
#         self.go_click=False
#         self.go_is_hover=False
#         self.go_border_color = (30,30,30)

        

#         #顯示判定
#         self.show_pika=False
#         self.show_gob=False
#         self.show_cat=False
        
#         self.flash_counter = 0
#         self.flash_speed = 5

        

#     def init_my_self(self):
        
#         self.pika_click=False
#         self.pika_box_color=(30,30,30)
#         self.gob_click=False
#         self.gob_box_color=(30,30,30)
#         self.cat_click=False
#         self.cat_box_color=(30,30,30)

#         self.gob_use_hover=True
#         self.cat_use_hover=True
#         self.pika_use_hover=True
    
#         self.go_click=False
#         self.go_box_color=(30,30,30) 

#         self.show_pika=False
#         self.show_gob=False
#         self.show_cat=False   

#     def update(self, events, screen):
#         #init       
#         if g_var.init_choose==True: 
#             self.init_my_self()
#             g_var.init_choose=False
        
#         for event in events:
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 raise SystemExit

#             if event.type == pygame.KEYDOWN :
#                 if event.key == pygame.K_ESCAPE:
#                     return "start"

#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 #pika的
#                 if self.pika_box.collidepoint(event.pos): #pika button
#                     if self.pika_click==False: #選pika
#                         self.pika_box_color=(100,100,100)
#                         g_var.point=21
#                         self.pika_use_hover=False
#                         self.pika_border_color = (30,30,30)
                        
#                         self.gob_box_color=(30,30,30)
#                         self.cat_box_color=(30,30,30)
#                         self.cat_use_hover=True
#                         self.gob_use_hover=True

#                         self.gob_click=False
#                         self.cat_click=False

#                         self.show_pika=True
#                         self.show_gob=False
#                         self.show_cat=False

#                         self.pika_click=True
#                     elif self.pika_click==True: #取消pika
#                         self.pika_box_color=(30,30,30)
#                         g_var.point=14
#                         self.pika_use_hover=True
#                         self.pika_click=False

#                         self.show_pika=False
#                 #pika的end
#                 #gob的
#                 if self.gob_box.collidepoint(event.pos): #gob button
#                     if self.gob_click==False: #選gob
#                         self.gob_box_color=(100,100,100)
#                         g_var.point=14
#                         self.gob_use_hover=False
#                         self.gob_border_color = (30,30,30)
                        
#                         self.pika_box_color=(30,30,30)
#                         self.cat_box_color=(30,30,30)
#                         self.cat_use_hover=True
#                         self.pika_use_hover=True

#                         self.pika_click=False
#                         self.cat_click=False

#                         self.show_pika=False
#                         self.show_gob=True
#                         self.show_cat=False

#                         self.gob_click=True
#                     elif self.gob_click==True: #取消gob
#                         self.gob_box_color=(30,30,30)
#                         g_var.point=14
#                         self.gob_use_hover=True
#                         self.gob_click=False
                        
#                         self.show_gob=False
#                 #gob的end
#                 #cat的
#                 if self.cat_box.collidepoint(event.pos): #cat button
#                     if self.cat_click==False: #選cat
#                         self.cat_box_color=(100,100,100)
#                         g_var.point=5
#                         self.cat_use_hover=False
#                         self.cat_border_color = (30,30,30)
                        
#                         self.pika_box_color=(30,30,30)
#                         self.gob_box_color=(30,30,30)
#                         self.gob_use_hover=True
#                         self.pika_use_hover=True

#                         self.pika_click=False
#                         self.gob_click=False

#                         self.show_pika=False
#                         self.show_gob=False
#                         self.show_cat=True

#                         self.cat_click=True
#                     elif self.cat_click==True: #取消cat
#                         self.cat_box_color=(30,30,30)
#                         g_var.point=14
#                         self.cat_use_hover=True
#                         self.cat_click=False

#                         self.show_cat=False
#                 #cat的end
                
#                 if self.go_box.collidepoint(event.pos):
#                     g_var.init_choose=True
#                     return "game"
      
#         #hover 
#         #pika
#         mouse_pos = pygame.mouse.get_pos()
#         if self.pika_use_hover==True:
#             if self.pika_box.collidepoint(mouse_pos):
#                 self.pika_box_color=(100,100,100)
#                 self.pika_is_hover=True

#                 # self.show_pika=True
#                 # self.show_gob=False
#                 # self.show_cat=False
#             else:
#                 self.pika_box_color=(30,30,30)
#                 self.pika_is_hover=False       
#         #gob
#         if self.gob_use_hover==True:
#             if self.gob_box.collidepoint(mouse_pos):
#                 self.gob_box_color=(100,100,100)
#                 self.gob_is_hover=True

#                 # self.show_pika=False
#                 # self.show_gob=True
#                 # self.show_cat=False
#             else:
#                 self.gob_box_color=(30,30,30)
#                 self.gob_is_hover=False
#         #cat
#         if self.cat_use_hover==True:
#             if self.cat_box.collidepoint(mouse_pos):
#                 self.cat_box_color=(100,100,100)
#                 self.cat_is_hover=True

#                 # self.show_pika=False
#                 # self.show_gob=False
#                 # self.show_cat=True
#             else:
#                 self.cat_box_color=(30,30,30)
#                 self.cat_is_hover=False
        
#         #go
#         if self.go_box.collidepoint(mouse_pos):
#             self.go_box_color=(100,100,100)
#             self.go_is_hover=True
#         else:
#             self.go_box_color=(30,30,30)
#             self.go_is_hover=False
        
#         self.flash_counter = (self.flash_counter + 1) % (self.flash_speed*2)
                    
        



#         return "point"

#     def draw(self, screen):
#         screen.fill((30, 30, 30))
        
#         #pika use hover
#         if self.pika_use_hover==True:
#             if self.pika_is_hover:
#                 if self.flash_counter < self.flash_speed:   
#                     self.pika_border_color = (233,199,19)  
#                 else:
#                     self.pika_border_color = (233,88,146)
#             else:
#                 self.pika_border_color = (30,30,30)
        
        
        
#         #gob use hover
#         if self.gob_use_hover==True:
#             if self.gob_is_hover:
#                 if self.flash_counter < self.flash_speed:   
#                     self.gob_border_color = (233,199,19)  
#                 else:
#                     self.gob_border_color = (233,88,146)
#             else:
#                 self.gob_border_color = (30,30,30)
        
        
#         #cat use hover
#         if self.cat_use_hover==True:
#             if self.cat_is_hover:
#                 if self.flash_counter < self.flash_speed:   
#                     self.cat_border_color = (233,199,19)  
#                 else:
#                     self.cat_border_color = (233,88,146)
#             else:
#                 self.cat_border_color = (30,30,30)
        
        

#         #go use hover
#         if self.go_is_hover:
#             if self.flash_counter < self.flash_speed:   
#                 self.go_border_color = (233,199,19)  
#             else:
#                 self.go_border_color = (233,88,146)
#         else:
#             self.go_border_color = (30,30,30)
        

#         pygame.draw.rect(screen, self.pika_box_color, self.pika_box,border_radius=10) #pika button
#         pygame.draw.rect(screen, self.pika_border_color, self.pika_box, width=6, border_radius=10) #閃
#         pygame.draw.rect(screen, self.gob_box_color, self.gob_box,border_radius=10) #gob button
#         pygame.draw.rect(screen, self.gob_border_color, self.gob_box, width=6, border_radius=10) #閃
#         pygame.draw.rect(screen, self.cat_box_color, self.cat_box,border_radius=10) #cat button
#         pygame.draw.rect(screen, self.cat_border_color, self.cat_box, width=6, border_radius=10) #閃
       
#         pygame.draw.rect(screen,self.go_box_color,self.go_box,border_radius=10)
#         pygame.draw.rect(screen, self.go_border_color, self.go_box, width=6, border_radius=10) #閃

#         screen.blit(self.pika_text, self.pika_text_center) #pika word
#         screen.blit(self.gob_text, self.gob_text_center) #gob word
#         screen.blit(self.cat_text, self.cat_text_center) #cat word
       
#         screen.blit(self.go_text,self.go_text_center)

#         # get_text=self.lable1.render(f"{g_var.get_char}",True,"white")
#         # screen.blit(get_text,(100,100))

#         text=self.lable1.render("p1 select char",True,"white")
#         middle=text.get_rect(center=(640,150))
#         screen.blit(text,middle)


#         # self.pika.draw(screen,200,500)
        





