# ui_elements.py
import pygame
import g_var
class TextButton:
    def __init__(self, text, font, center, padding=40, colors=((200,200,200),(100,100,100))):
        """
        text: 按鈕顯示文字
        font: pygame.font.Font
        center: (x, y) 中心位置
        padding: 文字與邊框的間隔
        colors: (文字顏色, hover 底色)
        """
        self.text = text
        self.font = font
        self.center = center
        self.padding = padding
        self.text_color, self.hover_color = colors

        # --- 繪製文字並建立矩形 ---
        self.surface = self.font.render(self.text, True, self.text_color)
        self.rect_text = self.surface.get_rect(center=self.center)
        self.rect_button = pygame.Rect(0, 0, self.rect_text.width + padding*2, self.rect_text.height + padding)
        self.rect_button.center = self.center

        # 狀態控制
        self.flash_counter = 0
        self.flash_speed = 5  # 控制邊框閃爍速度

    def update(self):
        self.flash_counter = (self.flash_counter + 1) % (self.flash_speed*2)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        is_hover = self.rect_button.collidepoint(mouse_pos)

        # hover 的時候有底色
        if is_hover:
            pygame.draw.rect(screen, self.hover_color, self.rect_button, border_radius=10)


        # 邊框閃爍
        if is_hover:
            if self.flash_counter < self.flash_speed :   
                border_color = (233,199,19)  
            else :
                border_color = (233,88,146)
        else:
            border_color = (30,30,30)

        pygame.draw.rect(screen, border_color, self.rect_button, width=6, border_radius=8)

        # 繪製文字
        screen.blit(self.surface, self.rect_text)

    def is_clicked(self, event):
        """檢查是否被點擊"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect_button.collidepoint(event.pos)
        return False

class TextButtonToggle:
    def __init__(self, text, font, center, padding=40, colors=((200,200,200), (100,100,100), (100,100,100))):
        """
        text: 按鈕顯示文字
        font: pygame.font.Font
        center: (x, y) 中心位置
        padding: 文字與邊框的間隔
        colors: (文字顏色, toggled 底色, 預設底色)
        """
        self.text = text
        self.font = font
        self.center = center
        self.padding = padding
        self.text_color, self.toggled_color, self.bg_color = colors

        # --- 繪製文字並建立矩形 ---
        self.surface = self.font.render(self.text, True, self.text_color)
        self.rect_text = self.surface.get_rect(center=self.center)
        self.rect_button = pygame.Rect(0, 0, self.rect_text.width + padding*2, self.rect_text.height + padding)
        self.rect_button.center = self.center

        # 狀態控制
        self.flash_counter = 0
        self.flash_speed = 5  # 控制邊框閃爍速度
        self.toggled = False  # 是否被按下

    def update(self):
        self.flash_counter = (self.flash_counter + 1) % (self.flash_speed*2)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        is_hover = self.rect_button.collidepoint(mouse_pos)
        

        # ---- 底色判斷 ----
        if self.toggled==True:  # 被按下 → 永遠保持 toggled 顏色
            pygame.draw.rect(screen, self.toggled_color, self.rect_button, border_radius=10)
        elif is_hover:   # hover 但沒被按下
            pygame.draw.rect(screen, self.bg_color, self.rect_button, border_radius=10)

        # ---- 邊框閃爍 ----
        if is_hover:
            if self.flash_counter < self.flash_speed:   
                border_color = (233,199,19)  
            else:
                border_color = (233,88,146)
        else:
            border_color = (30,30,30)

        pygame.draw.rect(screen, border_color, self.rect_button, width=6, border_radius=8)

        # ---- 繪製文字 ----
        screen.blit(self.surface, self.rect_text)

    def is_clicked(self, event):
        """檢查是否被點擊 (切換狀態)"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect_button.collidepoint(event.pos):
                self.toggled = not self.toggled
                return True
        return False
