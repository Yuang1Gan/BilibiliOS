from PIL import Image
import easygui

def open_image():
        while True:
            try:
                easygui.msgbox("请将文件放入系统根目录后运行该程序", "Zhulong Image Viewer")
                name = easygui.enterbox("请输入图片名(记得带上文件后缀名,不输入退出)", "Zhulong Image Viewer")
                if name == 'q':
                    break
                else:
                    Image_name = Image.open(name)
                    Image_name.show()

            except FileNotFoundError:
                easygui.msgbox("Zhulong Image Viewer无法找到该文件", "Zhulong Image Viewer")
            except AttributeError:
                easygui.msgbox("Zhulong Image Viewer在运行时发生错误,已退出，若是为了退出，请忽略", "Zhulong Image Viewer")
                break
