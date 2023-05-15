import pgzrun, easygui, datetime, OS_information, time, Ssize

import image
#窗口高度
def screensize():
    f = open('screensize', 'r', encoding = 'utf-8')
    a = f.read()
    f.readline()
    return a
def read_bgp_name():
    f = open('背景名', 'r', encoding = 'utf-8')
    n = f.read()
    f.close()
    return n
a = screensize()
big = a.split('X')
width = big[0]
height = big[1]

WIDTH = int(width)
HEIGHT = int(height)
state = '开机'  #系统状态
name = read_bgp_name()  #标准背景
#图标定义
IMVI = Actor('imvi')
c = Actor('change')
off = Actor('关机')
ifor = Actor('系统信息')
size = Actor('size')
login = Actor('登录')
#图标位置
c.y = 200
off.x = WIDTH // 2
off.y = HEIGHT - 40
ifor.y = 300
size.y = 400
login.x = WIDTH // 2
login.y = HEIGHT // 2
#绘制
def draw():
    global state, name
    if state == '开机':
        screen.blit('开机背景', (0, 0))
        screen.draw.text('Welcome! BilibiliOS!', (WIDTH // 2 - 100, 200), fontsize = 55)
        screen.draw.text('Poward by: G-DOS-UI 2.2', (WIDTH // 2 - 150, HEIGHT - 40), fontsize = 55,  )
        login.draw()

    elif state == '桌面':
        screen.clear()
        screen.blit(name, pos=(0, 0))
        IMVI.draw()
        c.draw()
        a = datetime.datetime.now()
        screen.draw.text(a.strftime('%Y-%m-%d %A %B %H:%M:%S'), (WIDTH - 287, HEIGHT- 39), fontsize = 25)
        off.draw()
        ifor.draw()
        size.draw()
    elif state == '关机':
        time.sleep(2)
        screen.clear()
        screen.blit('关机背景', (0, 0))
        screen.draw.text('BilibiliOS is Closing, Bye~', (WIDTH // 2 - 150, 200), fontsize = 55)
        state = '已关机'
    elif state == '已关机':
        time.sleep(3)
        exit()
def update():
    pass

#背景切换程序
def change():
    choice = easygui.choicebox("请选择壁纸", "壁纸切换工具", ['bilibili2023拜年纪1', 'bilibili2023拜年纪2', 'bilibili2023拜年纪3', 'bilibili2023拜年纪4', 'bilibili2023拜年纪5'])
    name = open('背景名', 'w', encoding = 'utf-8')
    name.write(choice)
    name.close()
    return choice
#鼠标事件
def on_mouse_down(pos, button):
    global state, name
    #是否点击应用程序
    if IMVI.collidepoint(pos) and button == mouse.LEFT and state == '桌面':
        image.open_image()
    if c.collidepoint(pos) and button == mouse.LEFT and state == '桌面':
        name = change()
    #关机
    if off.collidepoint(pos) and button == mouse.LEFT and state == '桌面':
        state = '关机'
    #应用程序
    if ifor.collidepoint(pos) and button == mouse.LEFT and state == '桌面':
        OS_information.window()
    if size.collidepoint(pos) and button == mouse.LEFT and state == '桌面':
        Ssize.screen_size()
    if login.collidepoint(pos) and button == mouse.LEFT and state == '开机':
        f = open('code', 'r', encoding = 'utf-8')
        input_code = easygui.enterbox('请输入密码', '登录')
        a = f.read()
        f.close()
        if input_code == a:
            state = '桌面'
        else:
            easygui.msgbox('密码错误，已关机')
            exit()

#开始运行
pgzrun.go()
