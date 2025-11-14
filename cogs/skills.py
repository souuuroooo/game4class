#skills.py
import pygame
import os
import g_var

class Skill:
    def __init__(self):
        self.x=1280
        self.y=720

        self.joes=[]
        self.jo = pygame.image.load(os.path.join("cogs","skills", f"jo_pika.png")).convert_alpha()
        smoll_jo = pygame.transform.scale(self.jo, (self.x, self.y))
        self.joes.append(smoll_jo)       

        self.joes_at=[]
        self.jo_at = pygame.image.load(os.path.join("cogs","skills", f"jo_pika1.png")).convert_alpha()
        smoll_jo = pygame.transform.scale(self.jo_at, (self.x, self.y))
        self.joes_at.append(smoll_jo)   

        self.gobs=[]
        self.gob = pygame.image.load(os.path.join("cogs","skills", f"jo_gob.png")).convert_alpha()
        smoll_gob = pygame.transform.scale(self.gob, (self.x, self.y))
        self.gobs.append(smoll_gob) 

        self.gobs_at=[]
        self.gob_at = pygame.image.load(os.path.join("cogs","skills", f"jo_gob1.png")).convert_alpha()
        smoll_gob = pygame.transform.scale(self.gob_at, (self.x, self.y))
        self.gobs_at.append(smoll_gob) 

        self.cats=[]
        self.ca = pygame.image.load(os.path.join("cogs","skills", f"cat_meme.png")).convert_alpha()
        smoll_cat = pygame.transform.scale(self.ca, (self.x, self.y))
        self.cats.append(smoll_cat) 

        self.jo_frame_index = 0
        self.jo_frame_delay = 2
        self.jo_frame_counter = 0
        self.max=0     

        self.turn_frames = []
        for i in range(28):   # 有25張
            turn = pygame.image.load(os.path.join("cogs","turn_screen", f"{i}.png")).convert_alpha()
            img = pygame.transform.scale(turn, (1280, 720))
            self.turn_frames.append(img)
            
        self.turn_frame_index = 0
        self.turn_frame_delay = 1
        self.turn_frame_counter = 0
    
    def init_my_self(self):
        self.max = 0
        self.turn_frame_index = 0
        self.x = 1280
        self.y = 720
        self.joes = [pygame.transform.scale(self.jo, (self.x, self.y))]
        self.jo_frame_counter = 0

 
    def update(self, events,screen):
        # 更新 jo (變大)
        self.jo_frame_counter += 1
        if self.jo_frame_counter >= self.jo_frame_delay:
            self.max+=1
            if self.max<40:
                #3 in one
                self.x+=8
                self.y+=4.5               
                smoll_jo = pygame.transform.scale(self.jo, (self.x, self.y))
                self.joes.append(smoll_jo)                    
                self.jo_frame_counter = 0
                
                smoll_jo = pygame.transform.scale(self.jo_at, (self.x, self.y))
                self.joes_at.append(smoll_jo)                    
                self.jo_frame_counter = 0
                        
                smoll_gob = pygame.transform.scale(self.gob, (self.x, self.y))
                self.gobs.append(smoll_gob)                    
                self.jo_frame_counter = 0 

                smoll_gob = pygame.transform.scale(self.gob_at, (self.x, self.y))
                self.gobs_at.append(smoll_gob)                    
                self.jo_frame_counter = 0 
         
                smoll_cat = pygame.transform.scale(self.ca, (self.x, self.y))
                self.cats.append(smoll_cat)                    
                self.jo_frame_counter = 0   
                
        
        if self.max>=40 and self.max<67:
            self.turn_frame_counter += 1
            if self.turn_frame_counter >= self.turn_frame_delay:
                self.turn_frame_index +=1
                self.turn_frame_counter = 0
            
        if self.max>=75:
            self.init_my_self()
            g_var.back_from_skill = True
            

            return "game"
                
        return "skill"


    def draw(self, screen):
        screen.fill((30, 30, 30))

        if g_var.skill_bg:
            screen.blit(g_var.skill_bg, (0, 0))

        if self.max >=67:
            screen.fill((0, 0, 0))
        
        if g_var.go_to_skill=="p1":
            if self.max<67:
                if g_var.get_char =="pika":
                    current_img = self.joes[-1]
                    rect = current_img.get_rect(center=(640, 360))  # 中心固定在視窗中心
                    screen.blit(current_img, rect)
                elif g_var.get_char=="gob":
                    current_img = self.gobs[-1]
                    rect = current_img.get_rect(center=(640, 360))  # 中心固定在視窗中心
                    screen.blit(current_img, rect)
                elif g_var.get_char=="cat":
                    current_img = self.cats[-1]
                    rect = current_img.get_rect(center=(640, 360))  # 中心固定在視窗中心
                    screen.blit(current_img, rect)

            if self.max>=40 and self.max<67:
                screen.blit(self.turn_frames[self.turn_frame_index], (0,0))
        
        if g_var.go_to_skill=="p2":
            if self.max<67:
                if g_var.get_char_2 =="pika":
                    current_img = self.joes_at[-1]
                    rect = current_img.get_rect(center=(640, 360))  # 中心固定在視窗中心
                    screen.blit(current_img, rect)
                elif g_var.get_char_2=="gob":
                    current_img = self.gobs_at[-1]
                    rect = current_img.get_rect(center=(640, 360))  # 中心固定在視窗中心
                    screen.blit(current_img, rect)
                elif g_var.get_char_2=="cat":
                    current_img = self.cats[-1]
                    rect = current_img.get_rect(center=(640, 360))  # 中心固定在視窗中心
                    current_img=pygame.transform.flip(current_img, True ,False)
                    screen.blit(current_img, rect)

            if self.max>=40 and self.max<67:
                screen.blit(self.turn_frames[self.turn_frame_index], (0,0))
        

