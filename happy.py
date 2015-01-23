import sys, pygame

pygame.init()
    
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def start():
    # Setup happy default values
    conf()
    # Declare and initialize game values
    load()

    # Game loop
    while True:
        # Handle events
        events()
        
        # Handle updates
        update()
        
        # Handle draw
        screen.fill(BLACK)
        draw()
        
        pygame.display.update()

def conf():
    return
    
def load():
    return

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.ACTIVEEVENT:
            active_event(event.gain, event.state)
        elif event.type == pygame.KEYDOWN:
            key_down(event.key, event.unicode, event.mod)
        elif event.type == pygame.KEYUP:
            key_up(event.key, event.uni, event.mod)
        elif event.type == pygame.MOUSEMOTION:
            mouse_motion(event.pos, event.rel, event.buttons)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_button_up(event.button, event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button_down(event.button, event.pos)
        elif event.type == pygame.JOYAXISMOTION:
            joy_axis_motion(event.joy, event.axis, event.value)
        elif event.type == pygame.JOYBALLMOTION:
            joy_ball_motion(event.joy, event.ball, event.rel)
        elif event.type == pygame.JOYHATMOTION:
            joy_hat_motion(event.joy, event.hat, event.value)
        elif event.type == pygame.JOYBUTTONUP:
            joy_button_up(event.joy, event.button)
        elif event.type == pygame.JOYBUTTONDOWN:
            joy_button_down(event.joy, event.button)
        elif event.type == pygame.VIDEORESIZE:
            video_resize(event.size, event.w, event.h)
        elif event.type == pygame.VIDEOEXPOSE:
            video_expose()
        elif event.type == pygame.USEREVENT:
            user_event(event.code)
    
def update():
    return
    
def draw():
    return
        
        
def quit():
    pygame.quit()
    sys.exit()

def loop(function):
    function_name = function.__name__.lower()
    underscore = "_"
    
    function_name = function_name.replace(underscore,'')
    
    if function_name == 'conf' or function_name == 'config':
        global conf
        conf = function
    elif function_name == 'load':
        global load
        load = function
    elif function_name == 'events':
        global events
        events = function
    elif function_name == 'update':
        global update
        update = function
    elif function_name == 'draw':
        global draw
        draw = function
    elif function_name == 'quit' or function_name == 'exit':
        global quit
        quit = function
    elif function_name == 'activeevent':
        global active_event
        active_event = function
    elif function_name == 'keydown':
        global key_down
        key_down = function
    elif function_name == 'keyup':
        global key_up
        key_up = function
    elif function_name == 'mousemotion':
        global mouse_motion
        mouse_motion = function
    elif function_name == 'mousebuttonup':
        global mouse_button_up
        mouse_button_up = function
    elif function_name == 'mousebuttondown':
        global mouse_button_down
        mouse_button_down = function
    elif function_name == 'joyaxismotion':
        global joy_axis_motion
        joy_axis_motion = function
    elif function_name == 'joyballmotion':
        global joy_ball_motion
        joy_ball_motion = function
    elif function_name == 'joyhatmotion':
        global joy_hat_motion
        joy_hat_motion = function
    elif function_name == 'joybuttonup':
        global joy_button_up
        joy_button_up = function
    elif function_name == 'joybuttondown':
        global joy_button_down
        joy_button_down = function
    elif function_name == 'videoresize':
        global video_resize
        video_resize = function
    elif function_name == 'videoexpose':
        global video_expose
        video_expose = function
    elif function_name == 'userevent':
        global user_event
        user_event = function

def active_event(gain, state=None):
    return

def key_down(key, uni=None, mod=None):
    return

def key_up(key, uni=None, mod=None):
    return
    
def mouse_motion(pos, rel=None, buttons=None):
    return
    
def mouse_button_up(button, pos=None):
    return
    
def mouse_button_down(button, pos=None):
    return
    
def joy_axis_motion(joy, axis, value=None):
    return
    
def joy_ball_motion(joy, ball, rel=None):
    return
    
def joy_hat_motion(joy, hat, value=None):
    return
    
def joy_button_up(joy, button):
    return
    
def joy_button_down(joy, button):
    return
    
def video_resize(size, w=None, h=None):
    return
    
def video_expose():
    return
    
def user_event(code):
    return
