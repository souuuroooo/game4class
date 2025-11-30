#game_scene.py
import pygame
import pymunk
import os
import g_var
from cogs.ui_elements import TextButton
from cogs.characters import Character
from cogs.backgrounds import Background

print(pymunk.version)



class GameScene:
    

    def __init__(self, width, height):
        

        def create_hitbox(space, box_size=(70, 20), init_pos=(-200, 350), body_type=pymunk.Body.KINEMATIC):
        
            mass = 1
            moment = pymunk.moment_for_box(mass, box_size)

            # 建立剛體與形狀
            body = pymunk.Body(mass, moment, body_type=body_type)
            body.position = init_pos

            shape = pymunk.Poly.create_box(body, box_size)
            shape.elasticity = 3
            shape.friction = 0.8

            # 加入物理空間
            space.add(body, shape)

            # 封裝成物件回傳
            return {
                "body": body,
                "shape": shape,
                "width": box_size[0],
                "height": box_size[1]
            }
        self.skill_active = False
        self.skill_timer = 0
        self.ball2_ground=False
        self.wait=0
        self.L_get_point=False
        self.R_get_point=False
        self.change_ball=False
        self.ball_count=1
    
        self.WIDTH, self.HEIGHT = width, height
        self.font = pygame.font.SysFont(None, 24)

        self.lable = pygame.font.SysFont("Microsoft JhengHei", 60)
        self.im_pause=TextButton("▋▋",self.lable,(1230,50))
        self.font_broad = pygame.font.SysFont(None, 60) 

        # ---- Pymunk ----
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)

        def pymunk_to_pygame(p): 
            return int(p[0]), int(self.HEIGHT - p[1])
        self.pymunk_to_pygame = pymunk_to_pygame       

        # 地板
        self.floor_y = 80
        floor_segment = pymunk.Segment(self.space.static_body, (0, self.floor_y), (self.WIDTH, self.floor_y), 5)
        floor_segment.friction = 0.8
        floor_segment.elasticity = 1
        self.space.add(floor_segment)    

        # 小球 1 其實是哥布林跟鼻孔
        self.radius = 40
        mass = 1
        moment = pymunk.moment_for_circle(mass, 0, self.radius)
        self.ball_body = pymunk.Body(mass, moment)
        self.start_x, self.start_y = 350, 150
        self.ball_body.position = (self.start_x, self.start_y)
        ball_shape = pymunk.Circle(self.ball_body, self.radius)
        ball_shape.elasticity = 0
        self.space.add(self.ball_body, ball_shape)

        #ball at
        self.radius = 40
        mass = 1
        moment = pymunk.moment_for_circle(mass, 0, self.radius)
        self.ball_at_body = pymunk.Body(mass, moment)
        self.start_x_at, self.start_y_at = 930, 150
        self.ball_at_body.position = (self.start_x_at, self.start_y_at)
        ball_shape = pymunk.Circle(self.ball_at_body, self.radius)
        ball_shape.elasticity = 0
        self.space.add(self.ball_at_body, ball_shape)

        # 小球 2
        self.small_radius=40
        moment = pymunk.moment_for_circle(mass, 0, self.radius)
        self.ball_body2 = pymunk.Body(mass, moment)
        self.start_x2, self.start_y2 = 300, self.HEIGHT - 200
        self.ball_body2.position = (self.start_x2, self.start_y2)
        ball_shape2 = pymunk.Circle(self.ball_body2, self.small_radius)
        ball_shape2.elasticity = 1
        self.space.add(self.ball_body2, ball_shape2)

    #p1 hit box
        #box above head 
        box_size = (80, 10)  # 寬, 高
        mass_box = 1
        moment_box = pymunk.moment_for_box(mass_box, box_size)

        self.box_body = pymunk.Body(mass_box, moment_box, body_type=pymunk.Body.KINEMATIC)  
        self.box_body.position = (self.start_x, self.start_y + self.radius + 10)  # 初始位置在球上方
        self.box_shape = pymunk.Poly.create_box(self.box_body, box_size)
        self.box_shape.elasticity = 2
        self.box_shape.friction = 0.8
        self.space.add(self.box_body, self.box_shape)
        self.box_w, self.box_h = box_size

        #box left  
        box_size = (10, 120)  # 寬, 高
        mass_box = 1
        moment_box = pymunk.moment_for_box(mass_box, box_size)

        self.box_body_left = pymunk.Body(mass_box, moment_box, body_type=pymunk.Body.KINEMATIC)  
        self.box_body_left.position = (self.start_x - self.radius - 20, self.start_y )  # 初始位置在球上方
        self.box_shape_left = pymunk.Poly.create_box(self.box_body_left, box_size)
        self.box_shape_left.elasticity = 2
        self.box_shape_left.friction = 0.8
        self.space.add(self.box_body_left, self.box_shape_left)
        self.box_w_left, self.box_h_left = box_size

        #box right  
        box_size = (10, 120)  # 寬, 高
        mass_box = 1
        moment_box = pymunk.moment_for_box(mass_box, box_size)

        self.box_body_right = pymunk.Body(mass_box, moment_box, body_type=pymunk.Body.KINEMATIC)  
        self.box_body_right.position = (self.start_x + self.radius + 20, self.start_y )  # 初始位置在球上方
        self.box_shape_right = pymunk.Poly.create_box(self.box_body_right, box_size)
        self.box_shape_right.elasticity = 2
        self.box_shape_right.friction = 0.8
        self.space.add(self.box_body_right, self.box_shape_right)
        self.box_w_right, self.box_h_right = box_size
    #p1 hit box end
    #p2 hit box  
        #box above head 
        box_size = (80, 10)  # 寬, 高
        mass_box = 1
        moment_box = pymunk.moment_for_box(mass_box, box_size)

        self.box_at_body = pymunk.Body(mass_box, moment_box, body_type=pymunk.Body.KINEMATIC)  
        self.box_at_body.position = (self.start_x_at, self.start_y_at + self.radius + 10)  # 初始位置在球上方
        self.box_at_shape = pymunk.Poly.create_box(self.box_at_body, box_size)
        self.box_at_shape.elasticity = 2
        self.box_at_shape.friction = 0.8
        self.space.add(self.box_at_body, self.box_at_shape)
        self.box_at_w, self.box_at_h = box_size

        #box left  
        box_size = (10, 120)  # 寬, 高
        mass_box = 1
        moment_box = pymunk.moment_for_box(mass_box, box_size)

        self.box_at_body_left = pymunk.Body(mass_box, moment_box, body_type=pymunk.Body.KINEMATIC)  
        self.box_at_body_left.position = (self.start_x_at - self.radius - 20, self.start_y_at )  # 初始位置在球上方
        self.box_at_shape_left = pymunk.Poly.create_box(self.box_at_body_left, box_size)
        self.box_at_shape_left.elasticity = 2
        self.box_at_shape_left.friction = 0.8
        self.space.add(self.box_at_body_left, self.box_at_shape_left)
        self.box_at_w_left, self.box_at_h_left = box_size

        #box right  
        box_size = (10, 120)  # 寬, 高
        mass_box = 1
        moment_box = pymunk.moment_for_box(mass_box, box_size)

        self.box_at_body_right = pymunk.Body(mass_box, moment_box, body_type=pymunk.Body.KINEMATIC)  
        self.box_at_body_right.position = (self.start_x_at + self.radius + 20, self.start_y_at )  # 初始位置在球上方
        self.box_at_shape_right = pymunk.Poly.create_box(self.box_at_body_right, box_size)
        self.box_at_shape_right.elasticity = 2
        self.box_at_shape_right.friction = 0.8
        self.space.add(self.box_at_body_right, self.box_at_shape_right)
        self.box_at_w_right, self.box_at_h_right = box_size
    #p2 hit box end
     
        #neko hitbox
        box_size = (500, 10)  # 寬, 高
        mass_box = 1
        moment_box = pymunk.moment_for_box(mass_box, box_size)
        self.neko_box_init=(-600,350)
        self.neko_box_body = pymunk.Body(mass_box, moment_box, body_type=pymunk.Body.KINEMATIC)  
        self.neko_box_body.position = self.neko_box_init  #中心
        self.neko_shape = pymunk.Poly.create_box(self.neko_box_body, box_size)
        self.neko_shape.elasticity = 20
        self.neko_shape.friction = 0.8
        self.space.add(self.neko_box_body, self.neko_shape)
        self.box_w_neko, self.box_h_neko = box_size

        box_size = (10, 200)  # 寬, 高
        mass_box = 1
        moment_box = pymunk.moment_for_box(mass_box, box_size)
        self.neko_box2_init=(-600,350)
        self.neko_box2_body = pymunk.Body(mass_box, moment_box, body_type=pymunk.Body.KINEMATIC)  
        self.neko_box2_body.position = self.neko_box2_init  #中心
        self.neko2_shape = pymunk.Poly.create_box(self.neko_box2_body, box_size)
        self.neko2_shape.elasticity = 20
        self.neko2_shape.friction = 0.8
        self.space.add(self.neko_box2_body, self.neko2_shape)
        self.box2_w_neko, self.box2_h_neko = box_size

        #gob skill hitbox
        self.A = [
                    (70, 200),(120, 160),(40,130),(90,130),(30,160),(130,110),(20,110),(20,65),(120,65),(150,60),(170,30)
                ]       
        self.gob_hitbox1= create_hitbox(self.space, box_size=(70, 20))
        self.gob_hitbox2 = create_hitbox(self.space, box_size=(20, 70))
        self.gob_hitbox3= create_hitbox(self.space, box_size=(70, 20))
        self.gob_hitbox4= create_hitbox(self.space, box_size=(70, 20))
        self.gob_hitbox5 = create_hitbox(self.space, box_size=(20, 70))
        self.gob_hitbox6 = create_hitbox(self.space, box_size=(20, 70))
        self.gob_hitbox7 = create_hitbox(self.space, box_size=(20, 70))
        self.gob_hitbox8= create_hitbox(self.space, box_size=(70, 20))
        self.gob_hitbox9= create_hitbox(self.space, box_size=(70, 20))
        self.gob_hitbox10= create_hitbox(self.space, box_size=(20, 70))
        self.gob_hitbox11= create_hitbox(self.space, box_size=(20, 70))
        self.gob_box_init=(-200,350)


        # 控制參數
        self.timer = 0
        self.timer_at = 0

        # 字體
        self.lable1 = pygame.font.SysFont("Microsoft JhengHei", 60)

        #初始背景
        self.cat_bg = Background("cat_bg",14)
        self.beach_bg = Background("beach_bg",7)
        self.forest_bg = Background("forest_bg",8)

        # 初始化角色
    
        self.pika = Character("pika", "pika", 25, (100,100))        
        self.gob  = Character("gob", "gob", 12, (120,120))
        self.cat  = Character("cat", "cats", 4, (190,190))

        # 邊界 
        static_body = self.space.static_body
        thickness = 5
        left_wall = pymunk.Segment(static_body, (0, 0), (0, 720), thickness)
        right_wall = pymunk.Segment(static_body, (1280, 0), (1280, 720), thickness)
        top_wall = pymunk.Segment(static_body, (0, 720), (1280, 720), thickness)
        bottom_wall = pymunk.Segment(static_body, (0, 0), (1280, 0), thickness)

        for wall in (left_wall, right_wall, top_wall, bottom_wall):
            wall.friction = 0.8
            wall.elasticity = 1
            self.space.add(wall)

        #網子
        self.widea=50
        self.highta=250
        self.xa=640 
        self.ya=250
        static_body = self.space.static_body
        rect = pymunk.Poly.create_box(static_body, (self.widea, self.highta))  # 寬, 高
        rect.body.position = (self.xa,self.ya)  # 矩形中心位置
        rect.friction = 1.0
        rect.elasticity = 1
        self.space.add(rect)

        #素材
        self.word = pygame.image.load(os.path.join("cogs","material", "A.png")).convert_alpha()       
        broad = pygame.image.load(os.path.join("cogs","material", "broad.png")).convert_alpha()
        self.broad = pygame.transform.scale(broad,(300,300))
        self.b_count=0
        net = pygame.image.load(os.path.join("cogs","material", "net.png")).convert_alpha()
        self.net=pygame.transform.scale(net,(self.widea+10,self.highta+10))
        neko = pygame.image.load(os.path.join("cogs","material", "nekoo.png")).convert_alpha()
        nekoo = pygame.transform.flip(neko,1,0)
        self.neko1=pygame.transform.scale(nekoo,(300,250))
        neko = pygame.image.load(os.path.join("cogs","material", "nekooo.png")).convert_alpha()
        nekoo = pygame.transform.flip(neko,1,0)
        self.neko2=pygame.transform.scale(nekoo,(500,250))
        self.neko_x=0
        self.neko_count=0
        self.vege1= pygame.image.load(os.path.join("cogs","material", "vege.png")).convert_alpha()
        self.vege2= pygame.image.load(os.path.join("cogs","material", "stone.png")).convert_alpha()
        self.vege3= pygame.image.load(os.path.join("cogs","material", "wuwa.png")).convert_alpha()
        for i in range(3):
            self.__dict__[f"vege{i+1}"]=pygame.transform.scale(self.__dict__[f"vege{i+1}"],(150,150))
            # self.__dict__[f"gob_hitbox{i+1}"]["body"].position = self.gob_box_init
        
        escape=pygame.image.load(os.path.join("cogs","material", "escape.png")).convert_alpha()
        self.escape=pygame.transform.scale(escape,(720,360))
        self.escape_pos=self.escape.get_rect(center=(720,200))
        #gif
        self.wuii = []
        for i in range(25):
            img = pygame.image.load(os.path.join("cogs","wuiiai", f"{i}.png")).convert_alpha()
            img = pygame.transform.scale(img, (150,150))
            self.wuii.append(img)

        self.jo_font = []
        for i in range(10):
            img = pygame.image.load(os.path.join("cogs","jojo_font", f"{i+1}.png")).convert_alpha()
            img = pygame.transform.scale(img, (150,150))
            self.jo_font.append(img)

        self.wuii_index = 0
        self.wuii_index_delay = 2
        self.wuii_counter = 0 

        #test
        self.mouse_x, self.mouse_y = 0, 0    

        #skill
        self.cast_timer_p1=600
        self.cast_timer_p2=600
    
    def init_my_self(self):
        g_var.restart=True
        g_var.restart_choose=True
        self.b_count=0
        g_var.L_point=0
        g_var.R_point=0
        g_var.use_broad=False
        self.skill_active=False
        self.skill_timer=0
        g_var.back_from_skill = False
        self.ball2_ground=False 
        self.wait=0 
        self.neko_x=0
        self.timer = 0
        self.timer_at = 0
        self.L_get_point=False
        self.R_get_point=False
        self.neko_box_body.position = self.neko_box_init
        self.neko_box2_body.position = self.neko_box2_init
        self.cast_timer_p1=600
        self.cast_timer_p2=600


    def i_want_wuii(self,screen,x,y):
        frame = self.wuii[self.wuii_index]
        screen.blit(frame, (x,y))     

    def update(self, events ,screen):       
        
        keys=pygame.key.get_pressed()
        if self.skill_active and g_var.who_skilled=="p2pika":
            a=1
        else:
            if keys[pygame.K_d] and self.ball_body.position.x<580:
                self.ball_body.position = (self.ball_body.position.x+10, self.ball_body.position.y)
            if keys[pygame.K_a] and self.ball_body.position.x>50:
                self.ball_body.position = (self.ball_body.position.x-10, self.ball_body.position.y)
            if self.skill_active and g_var.who_skilled=="p1cat":
                if keys[pygame.K_w] :
                    if abs(self.ball_body.position.y - (self.floor_y + self.radius)) < 20 :
                        self.ball_body.velocity = (self.ball_body.velocity.x, 700)
                        self.box_body.velocity=(self.ball_body.velocity.x, 700) 
                    if abs(self.ball_body.position.y - (310 + self.radius)) < 30 :
                        self.ball_body.velocity = (self.ball_body.velocity.x, 700)
                        self.box_body.velocity=(self.ball_body.velocity.x, 700) 
                    if self.ball_body.velocity.y<100:
                        self.ball_body.velocity = (self.ball_body.velocity.x,20)
                        self.box_body.velocity=(self.ball_body.velocity.x, 20)
                a=1
            else:
                if keys[pygame.K_w] :
                    if abs(self.ball_body.position.y - (self.floor_y + self.radius)) < 20:
                        self.ball_body.velocity = (self.ball_body.velocity.x, 700)
                        self.box_body.velocity=(self.ball_body.velocity.x, 700) 
                    if self.ball_body.velocity.y<100:
                        self.ball_body.velocity = (self.ball_body.velocity.x,20)
                        self.box_body.velocity=(self.ball_body.velocity.x, 20)     
        

        if self.skill_active and g_var.who_skilled=="p1pika":
            a=1
        else:
            if keys[pygame.K_RIGHT] and self.ball_at_body.position.x<1230:
                self.ball_at_body.position = (self.ball_at_body.position.x+10, self.ball_at_body.position.y)
            if keys[pygame.K_LEFT] and self.ball_at_body.position.x>720:
                self.ball_at_body.position = (self.ball_at_body.position.x-10, self.ball_at_body.position.y)
            if self.skill_active and g_var.who_skilled=="p2cat":
                if keys[pygame.K_UP] :
                    if abs(self.ball_at_body.position.y - (self.floor_y + self.radius)) < 20:
                        self.ball_at_body.velocity = (self.ball_at_body.velocity.x, 700)
                        self.box_at_body.velocity=(self.ball_at_body.velocity.x, 700)
                    if abs(self.ball_at_body.position.y - (310 + self.radius)) < 30:
                        self.ball_at_body.velocity = (self.ball_at_body.velocity.x, 700)
                        self.box_at_body.velocity=(self.ball_at_body.velocity.x, 700)
                    if self.ball_at_body.velocity.y<100:
                            self.ball_at_body.velocity = (self.ball_at_body.velocity.x,20)
                            self.box_at_body.velocity=(self.ball_at_body.velocity.x, 20)
            else:            
                if keys[pygame.K_UP] :
                    if abs(self.ball_at_body.position.y - (self.floor_y + self.radius)) < 20:
                        self.ball_at_body.velocity = (self.ball_at_body.velocity.x, 700)
                        self.box_at_body.velocity=(self.ball_at_body.velocity.x, 700)
                    if self.ball_at_body.velocity.y<100:
                            self.ball_at_body.velocity = (self.ball_at_body.velocity.x,20)
                            self.box_at_body.velocity=(self.ball_at_body.velocity.x, 20)
        
        
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # self.ball_body.position = (self.start_x, self.start_y)
                    # self.ball_body.velocity = (0, 0)
                    # self.ball_body.angular_velocity = 0

                    self.ball_body2.position = (self.start_x2, self.start_y2)
                    self.ball_body2.velocity = (0, 0)
                    self.ball_body2.angular_velocity = 0               

                if event.key == pygame.K_ESCAPE:
                    self.init_my_self()
                    return "start"   # 按 ESC 回到起始畫面

                if event.key == pygame.K_p :
                    return "pause"  

                if self.skill_active==False:
                    if event.key == pygame.K_g and self.cast_timer_p1>=600:
                        g_var.skill_bg = screen.copy()  # 把當前畫面存成 Surface
                        g_var.go_to_skill="p1"
                        g_var.who_skilled=g_var.go_to_skill+g_var.get_char
                        self.cast_timer_p1=0
                        return "skill"

                if self.skill_active==False:
                    if event.key == pygame.K_KP5 and self.cast_timer_p2>=600:
                        g_var.skill_bg = screen.copy()  # 把當前畫面存成 Surface
                        g_var.go_to_skill="p2"
                        g_var.who_skilled=g_var.go_to_skill+g_var.get_char_2
                        self.cast_timer_p2=0
                        return "skill"

                if event.key == pygame.K_y:
                    g_var.use_broad=True
                    g_var.R_point+=1
                
                if event.key == pygame.K_t:
                    g_var.use_broad=True
                    g_var.L_point+=1
                    self.change_ball=True

                # end skill
                if event.key == pygame.K_KP1:
                    self.skill_timer -=1
                
                if event.key == pygame.K_1:
                    self.skill_timer -=1

            
            if self.im_pause.is_clicked(event):
                return "pause"
        
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        #回到位置
        if g_var.restart==True:
            self.ball_body.position = (self.start_x, self.start_y)
            self.ball_body.velocity = (0, 0)
            self.ball_body.angular_velocity = 0

            self.ball_at_body.position = (self.start_x_at, self.start_y_at)
            self.ball_at_body.velocity = (0, 0)
            self.ball_at_body.angular_velocity = 0

            self.ball_body2.position = (self.start_x2, self.start_y2)
            self.ball_body2.velocity = (0, 0)
            self.ball_body2.angular_velocity = 0
            g_var.restart=False

        if self.ball2_ground==True:
            if self.R_get_point==True:
                self.ball_body2.position = (1280-self.start_x2, self.start_y2)
                self.ball_body2.velocity = (0, 0)
                self.ball_body2.angular_velocity = 0
                self.wait+=1
                if self.wait<90:
                    self.ball_body2.position = (1280-self.start_x2, self.start_y2)
                    self.ball_body2.velocity = (0, 0)
                    self.ball_body2.angular_velocity = 0
                else:
                    self.wait=0
                    self.ball2_ground=False
                    self.R_get_point=False
            
            if self.L_get_point==True:
                self.ball_body2.position = (self.start_x2, self.start_y2)
                self.ball_body2.velocity = (0, 0)
                self.ball_body2.angular_velocity = 0
                self.wait+=1
                if self.wait<90:
                    self.ball_body2.position = (self.start_x2, self.start_y2)
                    self.ball_body2.velocity = (0, 0)
                    self.ball_body2.angular_velocity = 0
                else:
                    self.wait=0
                    self.ball2_ground=False
                    self.L_get_point=False
                
        #cast count
        if self.cast_timer_p1<=600:
            self.cast_timer_p1+=1
        else:
            a=1
        if self.cast_timer_p2<=600:
            self.cast_timer_p2+=1
        else:
            a=1
        
        
        #啟動技能
        if g_var.back_from_skill:   #平衡性調整技能時長
            if g_var.who_skilled=="p1pika" or g_var.who_skilled=="p2pika":
                self.skill_active = True
                self.skill_timer = 10  # give pika 4s to show (60fps) 
                g_var.back_from_skill = False
            elif g_var.who_skilled=="p1cat" :
                self.skill_active = True
                self.skill_timer = 480
                self.ball_body.position=(100,600)
                g_var.back_from_skill = False
            elif g_var.who_skilled=="p2cat":
                self.skill_active = True
                self.skill_timer = 480
                self.ball_at_body.position=(1180,600)
                g_var.back_from_skill = False
            elif g_var.who_skilled=="p1gob" or g_var.who_skilled=="p2gob":
                self.skill_active = True
                self.skill_timer = 360
                g_var.back_from_skill = False

        if self.skill_active:
            if g_var.who_skilled=="p1pika" or g_var.who_skilled=="p2pika":
                # self.ball_body2.velocity = (0,0)
                a=1
            if g_var.who_skilled=="p1cat" or g_var.who_skilled=="p2cat": #neko animate
                if self.neko_x<360 :
                    self.neko_count+=1
                    #neko
                    if self.neko_count<12:
                        self.neko_now=self.neko1
                    elif self.neko_count<24:
                        self.neko_now=self.neko2
                    else:
                        self.neko_count=0
                #wuii
                self.wuii_counter += 1
                if self.wuii_counter >= self.wuii_index_delay:
                    self.wuii_index = (self.wuii_index + 1) % len(self.wuii)
                    self.wuii_counter = 0
        
        #判斷技能要結束沒
        if self.skill_active:
            if g_var.who_skilled=="p1cat" or g_var.who_skilled=="p2cat" or g_var.who_skilled=="p1gob" or g_var.who_skilled=="p2gob":
                self.skill_timer -= 1
            if self.skill_timer <= 0:
                self.skill_active = False
                self.neko_box_body.position = self.neko_box_init
                self.neko_box2_body.position = self.neko_box2_init         
                self.neko_x=0
                for i in range(len(self.A)):
                    self.__dict__[f"gob_hitbox{i+1}"]["body"].position = self.gob_box_init

        # 控制 timer → 移動
        if self.timer == 0:
            self.ball_body.velocity = (0, self.ball_body.velocity.y)
        else:
            self.ball_body.velocity = (self.timer * 4, self.ball_body.velocity.y)
        if self.timer_at == 0:
            self.ball_at_body.velocity = (0, self.ball_at_body.velocity.y)
        else:
            self.ball_at_body.velocity = (self.timer_at * 4, self.ball_at_body.velocity.y)

        # 更新物理
        dt = 1 / 60.0
        steps = 2
        for _ in range(steps):
            self.space.step(dt / steps)
            #timer LR move
            if self.timer > 0:
                self.timer -= 1
            elif self.timer < 0:
                self.timer += 1
            if self.timer_at > 0:
                self.timer_at -= 1
            elif self.timer_at < 0:
                self.timer_at += 1
        
        # p1 hit box follow
        self.box_body.position = (self.ball_body.position.x, self.ball_body.position.y + 65)
        self.box_body_left.position = (self.ball_body.position.x-70, self.ball_body.position.y )
        self.box_body_right.position = (self.ball_body.position.x+70, self.ball_body.position.y )
        # p2 hit box follow
        self.box_at_body.position = (self.ball_at_body.position.x, self.ball_at_body.position.y + 65)
        self.box_at_body_left.position = (self.ball_at_body.position.x-70, self.ball_at_body.position.y )
        self.box_at_body_right.position = (self.ball_at_body.position.x+70, self.ball_at_body.position.y )
        #neko hit box follow
        if self.skill_active==True:
            if g_var.who_skilled=="p1cat" :
                self.neko_box_body.position=(self.neko_x+50,320)
                self.neko_box2_body.position=(self.neko_x-200,200)
            if g_var.who_skilled=="p2cat" :
                self.neko_box_body.position=(self.WIDTH-self.neko_x+20,320) #250magic
                self.neko_box2_body.position=(self.WIDTH-self.neko_x+300,200)

            if g_var.who_skilled=="p1gob":               
                for i in range(len(self.A)):
                    dx, dy = self.A[i]
                    self.__dict__[f"gob_hitbox{i+1}"]["body"].position = (
                        self.ball_body.position.x + dx,
                        self.ball_body.position.y + dy
                    )
            if g_var.who_skilled=="p2gob":               
                for i in range(len(self.A)):
                    dx, dy = self.A[i]
                    self.__dict__[f"gob_hitbox{i+1}"]["body"].position = (
                        self.ball_at_body.position.x + dx,
                        self.ball_at_body.position.y + dy
                    )

        

        #背景動畫
        if g_var.get_bg=="cat":
            self.cat_bg.update()
        elif g_var.get_bg=="beach":
            self.beach_bg.update()
        elif g_var.get_bg=="forest":
            self.forest_bg.update()

        #腳色動畫 p1
        if g_var.get_char == "pika":
            self.pika.update()
        elif g_var.get_char == "gob":
            self.gob.update()
        elif g_var.get_char == "cat":
            self.cat.update()
        #p2
        if g_var.get_char_2 == "pika":
            self.pika.update()
        elif g_var.get_char_2 == "gob":
            self.gob.update()
        elif g_var.get_char_2 == "cat":
            self.cat.update()      

        #速限
        if self.ball_body2.velocity.y > 900:
            self.ball_body2.velocity=(self.ball_body2.velocity.x,900)
        if self.ball_body2.velocity.x > 900:
            self.ball_body2.velocity=(900,self.ball_body2.velocity.y)

        #broad
        if g_var.use_broad==True:
            self.b_count+=1
        else:
            self.b_count=0

        #球落地
        if self.ball_body2.position.y<140:
            if self.ball_count<3:
                self.ball_count+=1
            else :
                self.ball_count=1
            
            if self.ball_body2.position.x<640:
                g_var.R_point+=1
                self.ball2_ground=True
                self.R_get_point=True
                g_var.use_broad=True
                
            if self.ball_body2.position.x>=640:
                g_var.L_point+=1
                self.ball2_ground=True
                self.L_get_point=True
                g_var.use_broad=True

        #結算
        if g_var.L_point == g_var.point:
            self.init_my_self()
            return "win"
                

        return "game"

    def draw(self, screen):
        #畫背景
        if g_var.get_bg=="cat":
            self.cat_bg.draw(screen)
        if g_var.get_bg=="beach":
            self.beach_bg.draw(screen)
        if g_var.get_bg=="forest":
            self.forest_bg.draw(screen)
        
        #畫技能
        if self.skill_active:
            if g_var.who_skilled=="p1pika" or g_var.who_skilled=="p2pika":
                self.word = pygame.transform.scale(self.word, (500,500))
                screen.blit(self.word,(0,0))
                screen.blit(self.word,(780,220))
                self.word = pygame.transform.scale(self.word, (300,300))
                screen.blit(self.word,(0,420))
                screen.blit(self.word,(980,0))              
            if g_var.who_skilled=="p1cat":
                if self.neko_x<360:
                    self.neko_x+=1
                screen.blit(self.neko_now,(self.neko_x-200,390)) #200 magic
                # #畫hit box
                # box_pos = self.pymunk_to_pygame(self.neko_box_body.position)
                # rect = pygame.Rect(0, 0, self.box_w_neko , self.box_h_neko)
                # rect.center = box_pos
                # pygame.draw.rect(screen, (255, 0, 0), rect)
                # box_pos = self.pymunk_to_pygame(self.neko_box2_body.position)
                # rect = pygame.Rect(0, 0, self.box2_w_neko , self.box2_h_neko)
                # rect.center = box_pos
                # pygame.draw.rect(screen, (255, 0, 0), rect)
                #wuii
                self.i_want_wuii(screen,100,100)
                self.i_want_wuii(screen,1200,150)
                self.i_want_wuii(screen,300,600)
                self.i_want_wuii(screen,700,350)
                self.i_want_wuii(screen,840,260)
                self.i_want_wuii(screen,1000,580)
                self.i_want_wuii(screen,500,200)
            
            if g_var.who_skilled=="p2cat":
                if self.neko_x<360:
                    self.neko_x+=1
                img=pygame.transform.flip(self.neko_now,True,False)
                screen.blit(img,(self.WIDTH-self.neko_x-230,390)) #200是魔法
                # #畫hit box
                # box_pos = self.pymunk_to_pygame(self.neko_box_body.position)
                # rect = pygame.Rect(0, 0, self.box_w_neko , self.box_h_neko)
                # rect.center = box_pos
                # pygame.draw.rect(screen, (255, 0, 0), rect)
                # box_pos = self.pymunk_to_pygame(self.neko_box2_body.position)
                # rect = pygame.Rect(0, 0, self.box2_w_neko , self.box2_h_neko)
                # rect.center = box_pos
                # pygame.draw.rect(screen, (255, 0, 0), rect)
                #wuii
                self.i_want_wuii(screen,100,100)
                self.i_want_wuii(screen,1200,150)
                self.i_want_wuii(screen,300,600)
                self.i_want_wuii(screen,700,350)
                self.i_want_wuii(screen,840,260)
                self.i_want_wuii(screen,1000,580)
                self.i_want_wuii(screen,500,200)

            if g_var.who_skilled=="p1gob":
                pos = self.pymunk_to_pygame(self.ball_body.position)
                self.gob.draw(screen,pos[0]+50,pos[1],-10)
                self.gob.draw(screen,pos[0]+100,pos[1],-10)
                self.gob.draw(screen,pos[0]+150,pos[1],-10)
                self.gob.draw(screen,pos[0]+25,pos[1]-50,-10)
                self.gob.draw(screen,pos[0]+75,pos[1]-50,-10)
                self.gob.draw(screen,pos[0]+125,pos[1]-50,-10)
                self.gob.draw(screen,pos[0]+50,pos[1]-100,-10)
                self.gob.draw(screen,pos[0]+100,pos[1]-100,-10)
                self.gob.draw(screen,pos[0]+75,pos[1]-150,-10)
                #畫hit box                
                # for i in range(len(self.A)):
                #     box_pos = self.pymunk_to_pygame(self.__dict__[f"gob_hitbox{i+1}"]["body"].position)
                #     rect = pygame.Rect(0, 0, self.__dict__[f"gob_hitbox{i+1}"]["width"] , self.__dict__[f"gob_hitbox{i+1}"]["height"])
                #     rect.center = box_pos
                #     pygame.draw.rect(screen, (255, 0, 0), rect)

            if g_var.who_skilled=="p2gob":
                pos = self.pymunk_to_pygame(self.ball_at_body.position)
                self.gob.draw_flip(screen,pos[0]+50,pos[1],-10)
                self.gob.draw_flip(screen,pos[0]+100,pos[1],-10)
                self.gob.draw_flip(screen,pos[0]+150,pos[1],-10)
                self.gob.draw_flip(screen,pos[0]+25,pos[1]-50,-10)
                self.gob.draw_flip(screen,pos[0]+75,pos[1]-50,-10)
                self.gob.draw_flip(screen,pos[0]+125,pos[1]-50,-10)
                self.gob.draw_flip(screen,pos[0]+50,pos[1]-100,-10)
                self.gob.draw_flip(screen,pos[0]+100,pos[1]-100,-10)
                self.gob.draw_flip(screen,pos[0]+75,pos[1]-150,-10)
                #畫hit box              
                # for i in range(len(self.A)):
                #     box_pos = self.pymunk_to_pygame(self.__dict__[f"gob_hitbox{i+1}"]["body"].position)
                #     rect = pygame.Rect(0, 0, self.__dict__[f"gob_hitbox{i+1}"]["width"] , self.__dict__[f"gob_hitbox{i+1}"]["height"])
                #     rect.center = box_pos
                #     pygame.draw.rect(screen, (255, 0, 0), rect)  
        
        #畫網子
        # pos=(self.xa-(self.widea/2),720-self.ya-(self.highta/2),self.widea,self.highta)       
        # pygame.draw.rect(screen,(200,0,0),pos)
        adjust=65 #往下一點
        pos=(self.xa-(self.widea/2),720-self.ya-(self.highta/2)+35)        
        screen.blit(self.net,pos)

        # draw p1  
        ball_pos = self.pymunk_to_pygame(self.ball_body.position)
        if g_var.get_char == "pika":
            self.pika.draw_flip(screen, ball_pos[0],ball_pos[1], -10)
        elif g_var.get_char == "gob":
            self.gob.draw(screen,  ball_pos[0],ball_pos[1], -10)
        elif g_var.get_char == "cat":
            self.cat.draw(screen,  ball_pos[0],ball_pos[1], -25)
        else:
            ball_pos = self.pymunk_to_pygame(self.ball_body.position)
            pygame.draw.circle(screen, g_var.get_char, ball_pos, int(self.radius))

        #draw p2
        ball_at_pos = self.pymunk_to_pygame(self.ball_at_body.position)
        if g_var.get_char_2 == "pika":
            self.pika.draw(screen,  ball_at_pos[0],ball_at_pos[1], -10)
        elif g_var.get_char_2 == "gob":
            self.gob.draw_flip(screen,  ball_at_pos[0],ball_at_pos[1], -10)
        elif g_var.get_char_2 == "cat":
            self.cat.draw_flip(screen,  ball_at_pos[0],ball_at_pos[1], -25)
        else:
            ball_pos = self.pymunk_to_pygame(self.ball_at_body.position)
            pygame.draw.circle(screen, g_var.get_char_2, ball_pos, int(self.radius))
        

        # 地板
        p1 = self.pymunk_to_pygame((0, self.floor_y))
        p2 = self.pymunk_to_pygame((self.WIDTH, self.floor_y))
        pygame.draw.line(screen, (200, 200, 200), p1, p2, 5)

        #pause
        self.im_pause.update()
        self.im_pause.draw(screen)

        # 球             
        ball_pos2 = self.pymunk_to_pygame(self.ball_body2.position)
        # pygame.draw.circle(screen, "purple", ball_pos2, self.small_radius)

        # center = self.vege.get_rect(center=ball_pos2)  
        # screen.blit(self.vege, center)
        
        # if self.change_ball==True:
        #     if self.ball_count<3:
        #         self.ball_count+=1
                
        #     else:
        #         self.ball_count=1
        # self.change_ball==False       
        center = self.__dict__[f"vege{self.ball_count}"].get_rect(center=ball_pos2)  
        screen.blit(self.__dict__[f"vege{self.ball_count}"], center)

        # # 畫hit box
        # box_pos = self.pymunk_to_pygame(self.box_body.position)
        # rect = pygame.Rect(0, 0, self.box_w, self.box_h)
        # rect.center = box_pos
        # pygame.draw.rect(screen, (255, 0, 0), rect) 

        # box_pos = self.pymunk_to_pygame(self.box_body_left.position)
        # rect = pygame.Rect(0, 0, self.box_w_left, self.box_h_left)
        # rect.center = box_pos
        # pygame.draw.rect(screen, (255, 0, 0), rect) 

        # box_pos = self.pymunk_to_pygame(self.box_body_right.position)
        # rect = pygame.Rect(0, 0, self.box_w_right, self.box_h_right)
        # rect.center = box_pos
        # pygame.draw.rect(screen, (255, 0, 0), rect)
        # #p2
        # box_pos = self.pymunk_to_pygame(self.box_at_body.position)
        # rect = pygame.Rect(0, 0, self.box_at_w, self.box_at_h)
        # rect.center = box_pos
        # pygame.draw.rect(screen, (255, 0, 0), rect) 

        # box_pos = self.pymunk_to_pygame(self.box_at_body_left.position)
        # rect = pygame.Rect(0, 0, self.box_at_w_left, self.box_at_h_left)
        # rect.center = box_pos
        # pygame.draw.rect(screen, (255, 0, 0), rect) 

        # box_pos = self.pymunk_to_pygame(self.box_at_body_right.position)
        # rect = pygame.Rect(0, 0, self.box_at_w_right, self.box_at_h_right)
        # rect.center = box_pos
        # pygame.draw.rect(screen, (255, 0, 0), rect)       

        # 資訊
        message = self.font.render(f"{g_var.point},{g_var.L_point}", True, (240, 240, 240))
        screen.blit(message, (10, 10))

        message = self.font.render(f"CD:{10-int(self.cast_timer_p1/60)}", True, (240, 240, 240))
        screen.blit(message, (self.ball_body.position.x-50,720-self.ball_body.position.y-80))

        message = self.font.render(f"CD:{10-int(self.cast_timer_p2/60)}", True, (240, 240, 240))
        screen.blit(message, (self.ball_at_body.position.x-50,720-self.ball_at_body.position.y-80))

        # info = f"R=reset | Ball pos: ({self.ball_body.position.x:.1f}, {self.ball_body.position.y:.1f}) timer:{self.timer}"
        # img = self.font.render(info, True, (240, 240, 240))
        # screen.blit(img, (10, 10))

        # text1 = self.lable1.render(f"x:{self.mouse_x}", True, "red")
        # text2 = self.lable1.render(f"y:{self.mouse_y}", True, "red")
        # screen.blit(text1, (700,360))
        # screen.blit(text2, (700,260))

        # === 畫平台 ===
        # pygame.draw.rect(screen, (180, 180, 50), self.platform_rect)

        #broad
        if g_var.use_broad==True:
            if self.b_count <= 20:
                y = self.b_count * 5
            elif self.b_count <= 40:
                y = 100
            elif self.b_count <= 80:
                y = 100 - (self.b_count - 40) * 5
            else:
                y=-200
                g_var.use_broad=False 

            broad_copy = self.broad.copy()  
            text_R = self.font_broad.render(f"{g_var.R_point}", True, (0, 0, 0))  
            text_R_rect = text_R.get_rect(center=(220, 215))
            text_L = self.font_broad.render(f"{g_var.L_point}", True, (0, 0, 0))  
            text_L_rect = text_L.get_rect(center=(80, 215))
            text_mid = self.font_broad.render(":", True, (0, 0, 0)) 
            text_mid_rect = text_mid.get_rect(center=(150, 215)) 

            broad_copy.blit(text_mid, text_mid_rect)
            broad_copy.blit(text_L, text_L_rect)
            broad_copy.blit(text_R, text_R_rect) #文字貼到broad上 對broad來說的(150,215)
            rect = broad_copy.get_rect(center=(640, y))  
            screen.blit(broad_copy, rect)               
        

        #畫技能特效
        if self.skill_active:
            if g_var.who_skilled=="p1pika" or g_var.who_skilled=="p2pika":
                overlay = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
                overlay.fill((255, 255, 0, 100))  # 黃色透明
                screen.blit(self.escape,self.escape_pos)
                screen.blit(self.jo_font[self.skill_timer-1],(680,250))
                screen.blit(overlay, (0, 0))

                
            
            
        


