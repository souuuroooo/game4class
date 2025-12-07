#win.py
import pygame
import g_var
import os
import random
          
class victory:
    def read(self,file_name,d,frames,x=1,y=1):
        self.__dict__[f"emote{d}"]=[]
        for i in range(frames):
            img = pygame.image.load(os.path.join("cogs","emote",file_name, f"{i}.png")).convert_alpha()
            
            w, h = img.get_size()
            size=(int(w*x),int(h*y))
            img=pygame.transform.scale(img,size)
            self.__dict__[f"emote{d}"].append(img)
        
    def __init__(self):
        self.a=random.randint(1,3)
        # a=2
        if self.a==1:
            self.read("fin1",1,69)
            self.how_many=69
        if self.a==2:
            self.read("fin2",2,22,2,2)
            self.how_many=22
        if self.a==3:
            self.read("fin3",3,30)
            self.how_many=30
        
        self.frame_count=0
        self.frame_index=0

        self.lable1 = pygame.font.SysFont("Microsoft JhengHei", 60)
        
        self.text=self.lable1.render("nigro",True,"red")
        self.mock1=self.lable1.render("p1 too bad",True,"red")
        self.mock2=self.lable1.render("p2 too bad",True,"red")
        self.back=self.lable1.render("press esc to restart",True,"red")

        self.color=(30,30,30)
        self.flash_counter=0
        self.flash_speed=3
        
        self.pika_head = pygame.image.load(os.path.join("cogs","heads", "pika_head.png")).convert_alpha()
        w, h = self.pika_head.get_size()
        size=(int(w/2),int(h/2))
        self.pika_head=pygame.transform.scale(self.pika_head,size)    
        
        self.gob_head = pygame.image.load(os.path.join("cogs","heads", "gob_head.png")).convert_alpha()
        w, h = self.gob_head.get_size()
        size=(int(w),int(h))
        self.gob_head=pygame.transform.scale(self.gob_head,size) 

        self.cat_head = pygame.image.load(os.path.join("cogs","heads", "cat_head.png")).convert_alpha()
        w, h = self.cat_head.get_size()
        size=(int(w*1.2),int(h*1.5))
        self.cat_head=pygame.transform.scale(self.cat_head,size) 


        self.mock_counter=0

    def init_my_self(self):
        self.mock_counter=0
        

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
                    g_var.init_choose==True
                    return "start"
        

        self.frame_count+=1
        if self.frame_count>3:
            self.frame_index+=1
            self.frame_count=0
        if self.frame_index>=self.how_many:
            self.frame_index=0


        self.flash_counter+=1
        if self.flash_counter < self.flash_speed :   
            self.color = (233,199,19)  
        elif self.flash_counter < self.flash_speed*2:
            self.color = (233,88,146)
        else:
            self.flash_counter=0
            
        self.text=self.lable1.render(f"p{g_var.who_win}won!!",True,self.color)
        self.mock1=self.lable1.render("p1 too bad",True,self.color)
        self.mock2=self.lable1.render("p2 too bad",True,self.color)
        self.back=self.lable1.render("press esc to restart",True,self.color)

        self.mock_counter+=1

        return "win"

    def draw(self, screen):
        screen.fill((30,30,30))
        
        if g_var.who_win=="1":
            if self.mock_counter>=240:
                screen.blit(self.mock2,(100,300))
            if self.mock_counter>=120:
                rect=self.__dict__[f"emote{self.a}"][self.frame_index].get_rect(center=(520,460))
                screen.blit(self.__dict__[f"emote{self.a}"][self.frame_index],rect)
                if g_var.get_char=="pika":
                    screen.blit(self.pika_head,(450,220))
                if g_var.get_char=="gob":
                    screen.blit(self.gob_head,(370,220))
                if  g_var.get_char=="cat":
                    screen.blit(self.cat_head,(320,130))
            if self.mock_counter>=360:
                rect=self.__dict__[f"emote{self.a}"][self.frame_index].get_rect(center=(920,460))
                screen.blit(self.__dict__[f"emote{self.a}"][self.frame_index],rect)
                if g_var.get_char=="pika":
                    screen.blit(self.pika_head,(850,220))
                if g_var.get_char=="gob":
                    screen.blit(self.gob_head,(770,220))
                if  g_var.get_char=="cat":
                    screen.blit(self.cat_head,(720,130))
        
        if g_var.who_win=="2":
            if self.mock_counter>=240:
                screen.blit(self.mock1,(100,300))
            if self.mock_counter>=120:
                rect=self.__dict__[f"emote{self.a}"][self.frame_index].get_rect(center=(520,460))
                screen.blit(self.__dict__[f"emote{self.a}"][self.frame_index],rect)
                if g_var.get_char_2=="pika":
                    screen.blit(self.pika_head,(450,220))
                if g_var.get_char_2=="gob":
                    screen.blit(self.gob_head,(370,220))
                if  g_var.get_char_2=="cat":
                    screen.blit(self.cat_head,(320,130))
            if self.mock_counter>=360:
                rect=self.__dict__[f"emote{self.a}"][self.frame_index].get_rect(center=(920,460))
                screen.blit(self.__dict__[f"emote{self.a}"][self.frame_index],rect)
                if g_var.get_char_2=="pika":
                    screen.blit(self.pika_head,(850,220))
                if g_var.get_char_2=="gob":
                    screen.blit(self.gob_head,(770,220))
                if  g_var.get_char_2=="cat":
                    screen.blit(self.cat_head,(720,130))

        if self.mock_counter>=480:
            screen.blit(self.back,(100,400))
        
        
        rect=self.__dict__[f"emote{self.a}"][self.frame_index].get_rect(center=(720,360))
        screen.blit(self.__dict__[f"emote{self.a}"][self.frame_index],rect)
        screen.blit(self.text,(100,100))
        
        if g_var.who_win=="1" and g_var.get_char=="pika":
            screen.blit(self.pika_head,(650,120))
        if g_var.who_win=="1" and g_var.get_char=="gob":
            screen.blit(self.gob_head,(570,120))
        if g_var.who_win=="1" and g_var.get_char=="cat":
            screen.blit(self.cat_head,(520,30))
        if g_var.who_win=="2" and g_var.get_char_2=="pika":
            screen.blit(self.pika_head,(650,120))
        if g_var.who_win=="2" and g_var.get_char_2=="gob":
            screen.blit(self.gob_head,(570,120))
        if g_var.who_win=="2" and g_var.get_char_2=="cat":
            screen.blit(self.cat_head,(520,30))

#for pika center(-80,-240)
#for gob center(-150,-240)
#for cat center(-200,-330)

