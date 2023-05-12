import pgzrun, time, easygui
WIDTH = 500
HEIGHT = 500
OOBE_state = '确认安装'
start_init = Actor('开始安装')
start_init.x = 250
start_init.y = 250
def draw():
    global OOBE_state
    if OOBE_state == '确认安装':
        screen.blit('第一个界面', (0, 0))
        start_init.draw()
    elif OOBE_state == '开始安装':
        screen.blit('正在安装界面', (0, 0))
        screensize = open('screensize', 'w', encoding = 'utf-8')
        screensize.write('1700X860')
        name = open('背景名', 'w', encoding = 'utf-8')
        name.write('bilibili2023拜年纪1')
        screensize.close()
        name.close()
        OOBE_state = '注册'
    elif OOBE_state == '注册':
        time.sleep(10)
        code = open('code', 'w', encoding = 'utf-8')
        input_code = easygui.enterbox('请输入密码', '注册')
        code.write(input_code)
        code.close()
        easygui.msgbox('完成!')
        OOBE_state = '完成'
    elif OOBE_state == '完成':
        exit()
def on_mouse_down(pos, button):
    global OOBE_state
    if start_init.collidepoint(pos) and button == mouse.LEFT and OOBE_state == '确认安装':
        OOBE_state = '开始安装'

def update():
    pass
pgzrun.go()