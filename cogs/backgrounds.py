import pygame
import os

class Background:
    def __init__(self, folder, frame_count, size=(1280, 720)):
        """
        folder: 圖片資料夾名稱 (例如 "cat_bg")
        frame_count: 幾張圖片 (例如 14)
        size: 縮放大小 (預設 1280x720)
        """
        self.frames = []
        for i in range(frame_count):
            img = pygame.image.load(os.path.join("cogs",folder, f"{i}.png")).convert_alpha()
            scaled = pygame.transform.scale(img, size)
            self.frames.append(scaled)

        self.current_frame = 0
        self.frame_delay = 10  # 每多少更新一次影格
        self.counter = 0

    def update(self):
        """更新背景影格"""
        self.counter += 1
        if self.counter >= self.frame_delay:
            self.counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def draw(self, screen, pos=(0, 0)):
        """畫出背景"""
        screen.blit(self.frames[self.current_frame], pos)
