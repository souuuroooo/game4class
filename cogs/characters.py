# characters.py
import pygame, os

class Character:
    def __init__(self, name, folder, frame_count, size, flip_x=False, flip_y=False):
        self.name = name
        self.frames = []
        for i in range(frame_count):
            img = pygame.image.load(os.path.join("cogs",folder, f"{i}.png")).convert_alpha()
            img = pygame.transform.scale(img, size)
            img = pygame.transform.flip(img, flip_x, flip_y)
            self.frames.append(img)


        self.frame_index = 0
        self.frame_delay = 14
        self.frame_counter = 0

    def update(self,ticks=1):
        self.frame_counter += ticks
        if self.frame_counter >= self.frame_delay:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.frame_counter = 0

    def draw(self, screen, pos_x, pos_y, offset_y=0):
        frame = self.frames[self.frame_index]
        rect = frame.get_rect(center=(pos_x, pos_y + offset_y))
        frame=pygame.transform.flip(frame, False ,False)
        screen.blit(frame, rect)

    def draw_flip(self, screen, pos_x,pos_y, offset_y=0):
        frame = self.frames[self.frame_index]
        rect = frame.get_rect(center=(pos_x, pos_y + offset_y))
        frame=pygame.transform.flip(frame, True ,False)
        screen.blit(frame, rect)
