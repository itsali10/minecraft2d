import pygame as pg
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import math

def init_3d():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
    # Set up light position
    glLightfv(GL_LIGHT0, GL_POSITION, (1000, 1000, 1000, 0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.8, 0.8, 0.8, 1.0))

def sky():
    #glDisable(GL_DEPTH_TEST) 
    glBegin(GL_QUADS)
    glColor3f(135/255.0, 206/255.0, 235/255.0)  
    glVertex2f(-100000, -100000)
    glVertex2f(-100000, 100000)
    glVertex2f(100000, 100000)
    glVertex2f(100000, -100000)
    glEnd()
    #glEnable(GL_DEPTH_TEST)

def Block(xlevel,ylevel,type):
    glDisable(GL_DEPTH_TEST)
    x = xlevel * 64
    y = ylevel * 64

    if type == 'dirt':
        glBegin(GL_QUADS)
        glColor3f(185/255, 122/255, 87/255) 
        glVertex2f(x, y)
        glVertex2f(x, y+64)
        glVertex2f(x+64,y+64)
        glVertex2f(x+64,y)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(153/255, 101/255, 72/255) 
        glVertex2f(x+5, y+5)
        glVertex2f(x+5, y+59)
        glVertex2f(x+59,y+59)
        glVertex2f(x+59,y+5)
        glEnd()
    elif type == 'grass':
        glBegin(GL_QUADS)
        glColor3f(47/255, 242/255, 104/255) 
        glVertex2f(x, y+43)
        glVertex2f(x, y+64)
        glVertex2f(x+64,y+64)
        glVertex2f(x+64,y+43)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(42/255, 224/255, 96/255) 
        glVertex2f(x+5, y+53)
        glVertex2f(x+5, y+59)
        glVertex2f(x+59,y+59)
        glVertex2f(x+59,y+53)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(185/255, 122/255, 87/255) 
        glVertex2f(x, y)
        glVertex2f(x, y+48)
        glVertex2f(x+64,y+48)
        glVertex2f(x+64,y)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(153/255, 101/255, 72/255) 
        glVertex2f(x+5, y+5)
        glVertex2f(x+5, y+43)
        glVertex2f(x+59,y+43)
        glVertex2f(x+59,y+5)
        glEnd()
    elif type == 'stone':
        glBegin(GL_QUADS)
        glColor3f(127/255, 127/255, 127/255) 
        glVertex2f(x, y)
        glVertex2f(x, y+64)
        glVertex2f(x+64,y+64)
        glVertex2f(x+64,y)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(97/255, 97/255, 97/255) 
        glVertex2f(x+5, y+5)
        glVertex2f(x+5, y+59)
        glVertex2f(x+59,y+59)
        glVertex2f(x+59,y+5)
        glEnd()
    elif type == 'netherrack':
        glBegin(GL_QUADS)
        glColor3f(117/255, 0, 18/255) 
        glVertex2f(x, y)
        glVertex2f(x, y+64)
        glVertex2f(x+64,y+64)
        glVertex2f(x+64,y)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(77/255, 0, 12/255) 
        glVertex2f(x+5, y+5)
        glVertex2f(x+5, y+59)
        glVertex2f(x+59,y+59)
        glVertex2f(x+59,y+5)
        glEnd()
    elif type == 'wood':
        glBegin(GL_QUADS)
        glColor3f(185/255, 122/255, 87/255) 
        glVertex2f(x, y)
        glVertex2f(x, y+64)
        glVertex2f(x+64,y+64)
        glVertex2f(x+64,y)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(64/255, 42/255, 30/255)
        glVertex2f(x+5, y+5)
        glVertex2f(x+5, y+59)
        glVertex2f(x+59,y+59)
        glVertex2f(x+59,y+5)
        glEnd()
    elif type == 'leaf':
        glBegin(GL_QUADS)
        glColor3f(34/255, 177/255, 76/255) 
        glVertex2f(x, y)
        glVertex2f(x, y+64)
        glVertex2f(x+64,y+64)
        glVertex2f(x+64,y)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(22/255, 115/255, 49/255)
        glVertex2f(x+5, y+5)
        glVertex2f(x+5, y+59)
        glVertex2f(x+59,y+59)
        glVertex2f(x+59,y+5)
        glEnd()
    glEnable(GL_DEPTH_TEST)



def hotbar(selected_slot):
    glDisable(GL_DEPTH_TEST)
    for i in range(9):
        x = i * 120

        if i == selected_slot:
            glColor3f(1, 1, 1)
        else:
            glColor3f(0, 0, 0)

        glLineWidth(3)
        glBegin(GL_LINE_LOOP)
        glVertex2f(430 + x, 60)
        glVertex2f(430 + x, 160)
        glVertex2f(530 + x, 160)
        glVertex2f(530 + x, 60)
        glEnd()
    glEnable(GL_DEPTH_TEST)

def draw_block_outline(x, y):
    glDisable(GL_DEPTH_TEST)
    glColor3f(0, 0, 0)
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x * 64, y * 64)
    glVertex2f(x * 64, (y + 1) * 64)
    glVertex2f((x + 1) * 64, (y + 1) * 64)
    glVertex2f((x + 1) * 64, y * 64)
    glEnd()
    glEnable(GL_DEPTH_TEST)

def add_block_to_hotbar(hotbar_items, block_type):
    # First try to find a slot with the same block type
    for i, item in enumerate(hotbar_items):
        if item is not None and item[0] == block_type:
            current_type, current_count = item
            hotbar_items[i] = (block_type, current_count + 1)
            return True
    
    # If no matching slot, find an empty slot
    for i, item in enumerate(hotbar_items):
        if item is None:
            hotbar_items[i] = (block_type, 1)
            return True
    
    return False

def draw_3d_block(x, y, block_type, rotation):
    glPushMatrix()
    glTranslatef(x + 50, y + 50, 0)
    glRotatef(rotation, 0.5, 1, 0.3)
    glScalef(20, 20, 20)
    
    if block_type == 'dirt':
        top = (185/255, 122/255, 87/255)
        side = (153/255, 101/255, 72/255)
    elif block_type == 'grass':
        top = (47/255, 242/255, 104/255)
        side = (185/255, 122/255, 87/255)
    elif block_type == 'stone':
        top = (127/255, 127/255, 127/255)
        side = (97/255, 97/255, 97/255)
    elif block_type == 'netherrack':
        top = (117/255, 0, 18/255)
        side = (77/255, 0, 12/255)
    elif block_type == 'wood':
        top = (185/255, 122/255, 87/255)
        side = (64/255, 42/255, 30/255)
    elif block_type == 'leaf':
        top = (34/255, 177/255, 76/255)
        side = (22/255, 115/255, 49/255)
    else:
        top = (1.0, 1.0, 1.0)
        side = (0.8, 0.8, 0.8)

    glBegin(GL_QUADS)
    # Front face
    glColor3f(*side)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)

    # Right face
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)

    # Back face
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)

    # Left face
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    # Top face (lighter color)
    glColor3f(*top)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)

    # Bottom face
    glColor3f(*side)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glEnd()

    # Draw edges for better visibility
    glColor3f(0, 0, 0)
    glLineWidth(1.0)
    glBegin(GL_LINES)
    # Front face
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    # Back face
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    # Connecting lines
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glEnd()

    glPopMatrix()

def draw_item_in_hotbar(slot, item_data, rotation, number_textures):
    if item_data is None:
        return
        
    block_type, count = item_data
    x = 430 + (slot * 120)
    y = 60

    # Draw the 3D rotating block
    draw_3d_block(x, y, block_type, rotation)
    
    # Draw the count
    if count > 1:
        glDisable(GL_DEPTH_TEST)
        text_surface, (text_width, text_height) = number_textures[min(count, 64)]
        glWindowPos2i(int(x + 70), int(y + 70))
        glDrawPixels(text_width, text_height, GL_RGBA, GL_UNSIGNED_BYTE, text_surface)
        glEnable(GL_DEPTH_TEST)

def draw_player(x, y):
    # Convert world coordinates to screen coordinates
    screen_x = x * 64
    screen_y = y * 64
    
    # Draw player body (2 blocks tall, 0.6 blocks wide)
    glDisable(GL_DEPTH_TEST)
    
    # Head (upper block)
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.6, 0.4)  # Skin color
    glVertex2f(screen_x + 16, screen_y + 96)  # Top block is smaller for head
    glVertex2f(screen_x + 48, screen_y + 96)
    glVertex2f(screen_x + 48, screen_y + 128)
    glVertex2f(screen_x + 16, screen_y + 128)
    glEnd()

    # Body (lower block)
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.4, 0.8)  # Blue shirt
    glVertex2f(screen_x + 16, screen_y)  # Start 16 pixels in from left (for 32 pixel width)
    glVertex2f(screen_x + 48, screen_y)  # End 16 pixels from right
    glVertex2f(screen_x + 48, screen_y + 96)
    glVertex2f(screen_x + 16, screen_y + 96)
    glEnd()
    
    glEnable(GL_DEPTH_TEST)

def draw_sun(rotation):
    glPushMatrix()
    glDisable(GL_LIGHTING)  # Disable lighting for the sun
    
    # Position sun in top right
    glTranslatef(1700, 900, 0)
    glRotatef(rotation * 0.5, 0, 0, 1)
    
    # Draw the sun as a yellow circle
    glColor3f(1.0, 0.95, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    radius = 80  # Increased radius
    segments = 32
    for i in range(segments + 1):
        angle = i * (2.0 * math.pi / segments)
        glVertex2f(radius * math.cos(angle), radius * math.sin(angle))
    glEnd()
    
    # Draw sun rays
    glColor3f(1.0, 0.9, 0.0)
    glLineWidth(3.0)  # Thicker rays
    glBegin(GL_LINES)
    for i in range(12):
        angle = i * 30 * math.pi / 180
        glVertex2f(0, 0)
        glVertex2f(120 * math.cos(angle), 120 * math.sin(angle))  # Longer rays
    glEnd()
    
    glEnable(GL_LIGHTING)
    glPopMatrix()

def draw_cloud(x, y):
    glPushMatrix()
    glDisable(GL_LIGHTING)
    
    # Draw much bigger cloud shapes
    glColor3f(1.0, 1.0, 1.0)
    glTranslatef(x, y, 0)
    
    # Main cloud body - much larger sizes
    glBegin(GL_QUADS)
    # Center piece
    glVertex2f(-100, -30)
    glVertex2f(100, -30)
    glVertex2f(100, 30)
    glVertex2f(-100, 30)
    
    # Top bumps
    glVertex2f(-80, 10)
    glVertex2f(-20, 10)
    glVertex2f(-20, 50)
    glVertex2f(-80, 50)
    
    glVertex2f(20, 10)
    glVertex2f(80, 10)
    glVertex2f(80, 60)
    glVertex2f(20, 60)
    
    # Bottom bumps
    glVertex2f(-60, -50)
    glVertex2f(0, -50)
    glVertex2f(0, -10)
    glVertex2f(-60, -10)
    
    glVertex2f(20, -40)
    glVertex2f(70, -40)
    glVertex2f(70, -5)
    glVertex2f(20, -5)
    glEnd()
    
    glEnable(GL_LIGHTING)
    glPopMatrix()

def check_collision(x, y, world_blocks):
    # Convert player position to block grid coordinates with a smaller hitbox
    player_left = x + 0.25
    player_right = x + 0.75 
    player_bottom = y
    player_top = y + 1.8  # Player height is 1.8 blocks
    
    # Get block coordinates that the player might be colliding with
    min_block_x = int(player_left)
    max_block_x = int(player_right) + 1
    min_block_y = int(player_bottom)
    max_block_y = int(player_top) + 1
    
    # Check each potentially colliding block
    for block_x in range(min_block_x, max_block_x):
        for block_y in range(min_block_y, max_block_y):
            if (block_x, block_y) in world_blocks:
                # Precise collision check with block boundaries
                if (player_right > block_x and
                    player_left < block_x + 1 and
                    player_top > block_y and
                    player_bottom < block_y + 1):
                    return True
    
    return False

def check_specific_collision(x, y, dx, dy, world_blocks):
    new_x = x
    new_y = y
    
    if dx != 0:
        test_x = x + dx
        if check_collision(test_x, y, world_blocks):
            test_x = x
        new_x = test_x
    
    if dy != 0:
        test_y = y + dy
        if check_collision(new_x, test_y, world_blocks):
            test_y = y
            dy = 0
        new_y = test_y
            
    return new_x, new_y, dy

def generate_overworld_blocks():
    world_blocks = {}
    for i in range(-20, 20):
        world_blocks[(i, 5)] = 'grass'
        for j in range(3, 5):
            world_blocks[(i, j)] = 'dirt'
        for j in range(0, 3):
            world_blocks[(i, j)] = 'stone'
    for i in range(6,11):
        for j in range(9,12):
            world_blocks[(i,j)]='leaf'
    for i in range(6,10):
        world_blocks[(8,i)]= 'wood'
    return world_blocks

def main():
    pg.init()
    pg.font.init()
    font = pg.font.Font(None, 36)
    display = (1920, 1080)
    screen = pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    init_3d()
    
    selected_slot = 0
    rotation = 0
    world_blocks = generate_overworld_blocks()
    hotbar_items = [None] * 9
    
    clouds = [(400, 800), (1200, 900), (2000, 850)]
    cloud_speeds = [0.4, 0.3, 0.5]
    
    # Player state
    player_x = 0
    player_y = 6
    player_velocity_y = 0
    move_speed = 0.1
    is_jumping = False
    gravity = -0.03
    jump_strength = 0.35
    
    number_textures = {}
    for i in range(1, 65):
        text = font.render(str(i), True, (255, 255, 255))
        text_surface = pg.transform.flip(text, False, True)
        text_surface = pg.image.tostring(text_surface, 'RGBA')
        number_textures[i] = (text_surface, text.get_size())

    # Set up OpenGL
    glViewport(0, 0, 1920, 1080)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 1920, 0, 1080, -1000, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    clock = pg.time.Clock()
    camera_y = 0
    is_in_nether = False

    while True:
        try:
            player_velocity_y += gravity
            
            keys = pg.key.get_pressed()
            move_x = 0
            if keys[pg.K_a] or keys[pg.K_LEFT]: 
                move_x = -move_speed
            if keys[pg.K_d] or keys[pg.K_RIGHT]: 
                move_x = move_speed
            
            new_x = player_x
            if move_x != 0:
                test_x = player_x + move_x
                if not check_collision(test_x, player_y, world_blocks):
                    new_x = test_x
            
            new_y = player_y
            if player_velocity_y != 0:
                test_y = player_y + player_velocity_y
                if not check_collision(new_x, test_y, world_blocks):
                    new_y = test_y
                else:
                    if player_velocity_y < 0: 
                        is_jumping = False
                    player_velocity_y = 0
            
            player_x = new_x
            player_y = new_y
            
            if player_y < 0:
                if not is_in_nether:
                    new_world_blocks = {}
                    for (x, y) in world_blocks:
                        new_world_blocks[(x, y)] = 'netherrack'
                    world_blocks = new_world_blocks
                    is_in_nether = True
                else:
                    world_blocks = generate_overworld_blocks()
                    is_in_nether = False
                player_x = 0
                player_y = 6
                player_velocity_y = 0

            if (keys[pg.K_SPACE] or keys[pg.K_w] or keys[pg.K_UP]) and not is_jumping:
                if check_collision(player_x, player_y - 0.1, world_blocks):
                    player_velocity_y = jump_strength
                    is_jumping = True

            target_camera_y = max(0, player_y * 64 - 300)
            camera_y += (target_camera_y - camera_y) * 0.1

            mouse_x, mouse_y = pg.mouse.get_pos()
            mouse_y = 1080 - mouse_y
            block_x = mouse_x // 64
            block_y = (mouse_y + camera_y) // 64

            rotation = (rotation + 1) % 360

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pg.quit()
                        return
                    if K_1 <= event.key <= K_9:
                        selected_slot = event.key - K_1
                elif event.type == pg.MOUSEBUTTONDOWN:
                    try:
                        if event.button == 1: 
                            if selected_slot is None or selected_slot < 0 or selected_slot >= len(hotbar_items):
                                selected_slot = 0
                            if (block_x, block_y) in world_blocks:
                                block_type = world_blocks[(block_x, block_y)]
                                
                                found_slot = None
                                for i, item in enumerate(hotbar_items):
                                    if item is not None and item[0] == block_type:
                                        current_count = item[1]
                                        if current_count < 64:  
                                            found_slot = i
                                            selected_slot = i
                                            break
                                
                                if found_slot is not None:
                                    current_type, current_count = hotbar_items[found_slot]
                                    hotbar_items[found_slot] = (block_type, min(64, current_count + 1))
                                    del world_blocks[(block_x, block_y)]
                                else:
                                    if hotbar_items[selected_slot] is None:
                                        hotbar_items[selected_slot] = (block_type, 1)
                                        del world_blocks[(block_x, block_y)]
                                    else:
                                        for i, item in enumerate(hotbar_items):
                                            if item is None:
                                                hotbar_items[i] = (block_type, 1)
                                                del world_blocks[(block_x, block_y)]
                                                break
                        
                        elif event.button == 3:
                            if selected_slot is None or selected_slot < 0 or selected_slot >= len(hotbar_items):
                                selected_slot = 0
                            if hotbar_items[selected_slot] is not None and (block_x, block_y) not in world_blocks:
                                player_blocks = {
                                    (int(player_x - 0.25), int(player_y)),
                                    (int(player_x + 0.25), int(player_y)),
                                    (int(player_x - 0.25), int(player_y + 1)),
                                    (int(player_x + 0.25), int(player_y + 1))
                                }
                                if (block_x, block_y) not in player_blocks:
                                    block_type, count = hotbar_items[selected_slot]
                                    world_blocks[(block_x, block_y)] = block_type
                                    if count > 1:
                                        hotbar_items[selected_slot] = (block_type, count - 1)
                                    else:
                                        hotbar_items[selected_slot] = None
                    except Exception as e:
                        print(f"Error handling mouse click: {e}")
                        continue
            
            if is_in_nether:
                glClearColor(0.3, 0.0, 0.0, 1.0) 
            else:
                glClearColor(135/255.0, 206/255.0, 235/255.0, 1.0) 
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(0, 1920, 0, 1080, -1000, 1000)
            
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

            if not is_in_nether:
                draw_sun(rotation)
                for i in range(len(clouds)):
                    clouds[i] = (clouds[i][0] + cloud_speeds[i], clouds[i][1])
                    if clouds[i][0] > 2200:
                        clouds[i] = (-200, clouds[i][1])
                    draw_cloud(clouds[i][0], clouds[i][1])
            
            glTranslatef(0, -camera_y, 0)
            
            visible_range = 30
            center_x = int(player_x)
            visible_y_range = 20
            min_y = int(camera_y // 64) - 5
            max_y = min_y + visible_y_range
            
            for x in range(center_x - visible_range, center_x + visible_range):
                for y in range(min_y, max_y):
                    if (x, y) in world_blocks:
                        Block(x, y, world_blocks[(x, y)])
            
            draw_player(player_x, player_y)
            
            draw_block_outline(block_x, block_y)
            
            glLoadIdentity()
            hotbar(selected_slot)
            
            for slot, item in enumerate(hotbar_items):
                if item is not None:
                    draw_item_in_hotbar(slot, item, rotation, number_textures)
            
            pg.display.flip()
            clock.tick(60)

        except Exception as e:
            print(f"Error in main loop: {e}")
            continue

main()