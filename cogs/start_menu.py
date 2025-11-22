import pygame
import os
from cogs.ui_elements import TextButton
import g_var
from cogs.characters import Character
import math
# from frog import Frog   # 把 Frog 類別也抽出去的話可以這樣用


wide = 1280

class StartMenu:
    def box(self,center):
        box=pygame.Rect(0,0,100,100)
        box.center=center
        return box
    def __init__(self):
        # --- 使用 TextButton ---
        self.lable1 = pygame.font.SysFont("Microsoft JhengHei", 60)
        self.lable2 = pygame.font.SysFont("Microsoft JhengHei", 36)
        self.start_button = TextButton("點擊或按Enter開始", self.lable1, (640, 360))
        self.exit_button = TextButton("退出遊戲", self.lable2, (640, 560))
        self.text2 = self.lable2.render("這好難我要暴斃了", True, (200,200,200))
        self.text2_rect = self.text2.get_rect(center=(640, 465))

        
        
        self.credits=TextButton("credits",self.lable1,(640,100))
        
        self.frog=Character("frog","images",10,(100,100))

        self.current_frame = 0
        self.frame_delay = 5
        self.counter = 0

        self.A=[
            (100, 100),
            (200, 200),
            (150, 120),
            (200, 500),
            (350, 420),
            (400, 600),
            (750, 130),
            (wide-100, 100),
            (wide-150, 120),
            (wide-200, 500),
            (wide-350, 420),
            (wide-400, 600),
            (wide-750, 130),
        ]
        self.boxes=[]
        self.look_press=[]
        for i in range(len(self.A)):
            self.boxes.append(self.box(self.A[i]))
            self.look_press.append(0) #1is ture
        
        y_sui=pygame.image.load(os.path.join("cogs","material", "y_sui.png")).convert_alpha()
        self.y_sui=pygame.transform.scale(y_sui,(500,700))

        y_sui=pygame.image.load(os.path.join("cogs","material", "y_sui2.png")).convert_alpha()
        self.y_sui2=pygame.transform.scale(y_sui,(280,360))

        self.flash_timer = 0
        self.flash_alpha = 255
        self.sui_timer=0
    def update(self, events,screen):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if self.start_button.is_clicked(event):
                g_var.init_choose=True
                return "p1"
            if self.exit_button.is_clicked(event): #is_clicked在ui裡
                pygame.quit()
                raise SystemExit
            if self.credits.is_clicked(event) and all(x == 1 for x in self.look_press):
                self.look_press.append(0)
                self.sui_timer=360
                return "credit"

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                g_var.init_choose=True
                return "p1"
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i in range (len(self.A)):
                    if self.boxes[i].collidepoint(event.pos):
                        self.look_press[i]=1
                


        self.frog.update(3)

        return "start"

    def draw(self, screen):
        screen.fill((30, 30, 30))

        # --- 更新按鈕狀態 ---
        self.start_button.update()
        self.exit_button.update()


        # --- 畫出按鈕 ---
        self.start_button.draw(screen)
        self.exit_button.draw(screen)
        

        # --- 額外文字 ---
        screen.blit(self.text2, self.text2_rect)

        # --- Frog & Boxes ---
        for i in range(len(self.A)):        
            if self.look_press[i] == 0:
                # pygame.draw.rect(screen,"red",self.boxes[i])
                self.frog.draw(screen, self.A[i][0], self.A[i][1])

        # --- 所有方塊按完之後 ---
        if all(x == 1 for x in self.look_press):
            self.sui_timer+=1
        # --- 閃爍效果 ---
            if self.sui_timer<360:
                self.flash_timer += 0.08
                self.flash_alpha = (math.sin(self.flash_timer) + 1) / 2 * 255
                self.y_sui.set_alpha(int(self.flash_alpha))

                self.y_sui2.set_alpha(int(self.flash_alpha))

                screen.blit(self.y_sui2, (500,0))
                screen.blit(self.y_sui2, (500,360))

                screen.blit(self.y_sui, (0,0))
                screen.blit(self.y_sui, (780,0))
                self.credits.update()
                self.credits.draw(screen)



