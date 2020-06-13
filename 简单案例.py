'''
尝试用python对大漠插件进行初步的封装
基本的按键和鼠标功能已经能够满足
更多功能函数请查阅《大漠接口说明》

后台键鼠模拟以及部分高级功能需要付费，注册后才能使用，我的注册码应该能用很久~
'''
from time import sleep
from damo import DM, Mouse, Key, vk

dm = DM()           # 初始化
#dm.reg()           # 注册
dm.Beep(500,550)    # 蜂鸣器


## 绑定窗口，实现后台键鼠操作。可同时创建多个dm对象
# dm.BindWindow(hwnd,display,mouse,keypad,mode)      # 若使用不了估计是欠费了，不搞违法事情用前台模拟就足够了……
# dm.UnBindWindow()


# 基本的鼠标操作
ms = Mouse()                        # 生成一个新的大漠鼠标对象
ms = Mouse(dm)                      # 继承旧的大漠鼠标对象，用于后台鼠标，建议使用这种

ms.position()                       # 当前鼠标位置

x, y = (0, 0)
ms.move_to(x, y)                    # 移动鼠标
ms.LeftClick()                      # 单击

# 组合功能
ms.test_click_right(x, y, 2, 1)     # 测试用, 延迟1秒后, 右键单击(x,y)位置，按下抬起的间隔为 2s

sleep(1)
ms.click_left(x, y, 2)              # 左键单击(x,y)位置, 默认按下抬起的间隔为2s
sleep(1)
ms.click_right(x, y)                # 右键单击(x,y)位置, 按下抬起的间隔为0.5s


# 键盘操作
kk = Key(dm)

kk.test_dp('a', 1)                  # 测试用, 1秒后按下a键
kk.dp('a')                          # 按下a键
kk.test_dp(vk.enter, 1)             # 测试enter键

# 全选操作
sleep(1)
kk.down(vk.ctrl)
kk.down('a')
kk.up(vk.ctrl)
kk.up('a')


# 像素颜色捕捉
from my_time import Time
tt = Time()
while(tt.during(10)):               # 10s内捕捉鼠标当前位置的颜色
    tt.sleep(0.1)

    x, y = ms.position()
    color = dm.GetColor(x, y)

    print(tt.now().__round__(1), color)


'''
图片查找案例：     https://github.com/bode135/YellowCard/blob/master/yellow_card/yellow_card_test.py

dm.Capture(x1, y1, x2, y2, file)                     # 截图并保存: dm.Capture(0,0,2000,2000,"screen.bmp")
dm.FindPic(x1, y1, x2, y2, pic_name, delta_color='101010', sim=0.9, dir=0, intX=0, intY=0)     # 图片查找
'''

'''
LOL按键型脚本： https://github.com/bode135/YellowCard
CF手游内存型外挂： https://github.com/bode135/CF-Flying
'''
