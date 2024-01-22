"""
像素颜色捕捉
"""

from pydamo import Time, DM, Mouse, Key, vk

dm = DM()
# dm.reg(your_register_code)
# dm.unreg_dm()

ms = Mouse(dm)
kk = Key(dm)
tt = Time()

dm.Beep()  # 蜂鸣器


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
