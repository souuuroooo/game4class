import pygame
import os
from cogs.ui_elements import TextButton
import g_var
# from frog import Frog   # 把 Frog 類別也抽出去的話可以這樣用


wide = 1280
class Frog:
    def __init__(self, frames, x, y):
        self.frames = frames
        self.x = x
        self.y = y
        self.current_frame = 0

    def draw(self, screen):
        screen.blit(self.frames[self.current_frame], (self.x, self.y))

class StartMenu:
    def __init__(self):
        self.lable1 = pygame.font.SysFont("Microsoft JhengHei", 60)
        self.lable2 = pygame.font.SysFont("Microsoft JhengHei", 36)

        # --- 載入動畫影格 ---
        self.frames = []
        for i in range(10):
            frog_ = pygame.image.load(os.path.join("cogs","images", f"frog_{i}.png")).convert_alpha()
            frog_small = pygame.transform.scale(frog_, (100, 100))
            self.frames.append(frog_small)

        self.current_frame = 0
        self.frame_delay = 5
        self.counter = 0

        # --- 建立青蛙們 ---
        self.frogs = [
            Frog(self.frames, 100, 100),
            Frog(self.frames, 200, 200),
            Frog(self.frames, 150, 120),
            Frog(self.frames, 200, 500),
            Frog(self.frames, 350, 420),
            Frog(self.frames, 400, 600),
            Frog(self.frames, 750, 130),
            Frog(self.frames, wide-100, 100),
            Frog(self.frames, wide-150, 120),
            Frog(self.frames, wide-200, 500),
            Frog(self.frames, wide-350, 420),
            Frog(self.frames, wide-400, 600),
            Frog(self.frames, wide-750, 130),
        ]

        # --- 使用 TextButton ---
        self.start_button = TextButton("點擊或按Enter開始", self.lable1, (640, 360))
        self.exit_button = TextButton("退出遊戲", self.lable2, (640, 560))
        self.text2 = self.lable2.render("這好難我要暴斃了", True, (200,200,200))
        self.text2_rect = self.text2.get_rect(center=(640, 465))

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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                g_var.init_choose=True
                return "p1"
        return "start"

    def draw(self, screen):
        screen.fill((30, 30, 30))

        # --- 更新動畫 ---
        self.counter += 1
        if self.counter >= self.frame_delay:
            self.counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            for frog in self.frogs:
                frog.current_frame = self.current_frame

        # --- 更新按鈕狀態 ---
        self.start_button.update() #update在ui裡
        self.exit_button.update()

        # --- 畫出按鈕 ---
        self.start_button.draw(screen)
        self.exit_button.draw(screen)

        # --- 額外文字 ---
        screen.blit(self.text2, self.text2_rect)

        # --- 繪製青蛙 ---
        for frog in self.frogs:
            frog.draw(screen)
