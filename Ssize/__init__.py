import easygui
def screen_size():
    while True:
        file = open('screensize', 'w', encoding = 'utf-8')
        #size = file.read()
        screensize = easygui.enterbox("请输入窗口大小, 格式：____X____", "窗口大小")
        if 'X' not in screensize:
            easygui.msgbox('格式错误，请重试', '窗口大小')
            continue
        file.write(screensize)
        file.close()
        easygui.msgbox('完成! 请重启系统', '窗口大小')
        break
#screen_size()