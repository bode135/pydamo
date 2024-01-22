"""
examples

- 后台按键需要注册, 需要付费购买注册码, 参考接口说明文件夹
"""

from pydamo import Time, DM, Mouse, Key, vk

dm = DM()
# dm.reg(your_register_code)
# dm.unreg_dm()

ms = Mouse(dm)
kk = Key(dm)
tt = Time()

dm.Beep()  # 蜂鸣器

# # ---------------- mouse simulation ---------------
# print(f'Mouse position: {ms.position}')  # 当前鼠标位置
#
# tt.sleep(1)
# x, y = (1000, 500)
# ms.move_to(x, y)  # 移动鼠标_1
#
# tt.sleep(1)
# x, y = (0, 0)
# ms.position = x, y  # 移动鼠标_2
#
# xy = (-100, 0)
# dm.MoveR(*xy)
#
# tt.sleep(1)
# ms.click_right(x, y)  # 右键单击(x,y)位置, 按下抬起的间隔为0.5s
#
# tt.sleep(1)
# x, y = (1000, 500)
# ms.click_left(x, y, 2)  # 左键单击(x,y)位置, 默认按下抬起的间隔为2s
#
# # ------------ key simulation -----------------------
# tt.sleep(1)
# kk.dp('a')  # 按下a键
# tt.sleep(1)
# kk.dp(vk.enter, 1)  # 测试enter键
#
# # 全选操作
# tt.sleep(1)
# kk.down(vk.ctrl)
# kk.down('a')
# kk.up(vk.ctrl)
# kk.up('a')


# 像素颜色捕捉
def conv_to_rgb(color):
    RGB_str = [color[:2], color[2:-2], color[-2:]]
    RGB = [int(i, 16) for i in RGB_str]
    return RGB


tt.__init__()
while tt.during(10):  # 10s内捕捉鼠标当前位置的颜色
    tt.sleep(0.1)

    if tt.get_key_state(vk.mouse_right) or tt.is_pressed('alt + x'):
        print('--- stopped!')
        break  # 按下鼠标右键, 或者`alt + x`, 则退出循环

    # tt.stop_alt('s')  # 按下`alt + s`则停止进程

    x, y = ms.position
    color = dm.GetColor(x, y)

    print(tt.now(1), color, '鼠标位置颜色RGB值:', conv_to_rgb(color))
