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
# self.__dict__[f"vege{i+1}"]=pygame.transform.scale(self.__dict__[f"vege{i+1}"],(150,150))
        
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
            
        

    def init_my_self(self):
        pass
        

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
        

        self.frame_count+=1
        if self.frame_count>3:
            self.frame_index+=1
            self.frame_count=0
        if self.frame_index>=self.how_many:
            self.frame_index=0
            


        return "win"

    def draw(self, screen):
        screen.fill((30,30,30))
        rect=self.__dict__[f"emote{self.a}"][self.frame_index].get_rect(center=(720,360))
        screen.blit(self.__dict__[f"emote{self.a}"][self.frame_index],rect)
        





