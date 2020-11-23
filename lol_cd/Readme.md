# 卡CD脚本实现过程
> **Bug原理:** <br>
> 出耀光后，空放一个技能，然后把耀光和正在冷却的装备E换位置，再平A触发耀光，这时候就直接刷新装备E的CD为1.5秒了。
## 初始化
> 核心开发包是驱动级按键模拟[`pydamo项目`](https://github.com/bode135/pydamo),<br>
> 更多细节可参考该项目的使用案例.
```
from pydamo_0 import Time, DM, Mouse, Key, vk
import os

dm = DM()
ms = Mouse(dm)
kk = Key(dm)
tt = Time()
```
## 参数设置
> 装备栏的第1&2格坐标自己用wx或者qq的截图确定就行.
> <br>大家的分辨率和用户界面不同, 需要自己设置.
```
tmp = 0.5           # 按键间隔
xy1 = (1095, 1005)  # 装备栏第1格的坐标
xy2 = (1125, 1005)  # 装备栏第2格的坐标
```
## 核心功能的实现
> 
```
# 将xy2的耀光移动到xy1， 然后鼠标移回xy0
def change_position(xy1=xy1, xy2=xy2, tmp = 0.1, ret_original_pos = 1):
    xy0 = ms.position
    ms.position = xy1
    dm.LeftDown()
    tt.sleep(tmp)
    ms.position = xy2
    dm.LeftUp()
    tt.sleep(tmp)

    # 返回原来的鼠标位置
    if(ret_original_pos):    ms.position = xy0

# 释放技能后调用该函数就可以自动刷新装备CD了，注意要把“快捷移动攻击指令”设置为字母“O”键。
def fresh_cd(ch = vk.o, xy1=xy1, xy2=xy2, tmp = 0.1, ret_original_pos = 1):
    change_position(xy1 = xy1, xy2 = xy2, tmp = tmp, ret_original_pos = ret_original_pos)
    kk.dp(ch)

# --- test ---
# tt.sleep(1)]
# change_position(xy1, xy2)
```
# 主函数编写
> 脚本会一直循环检测是否按下快捷键"["键 (vk.symbol[']'], 我的鼠标宏快捷键).
> <br>然后需要将游戏里的快捷攻击绑定为字母:O"键 (vk.o)
> <br>使用状态模式来切换脚本的[暂停/运行]状态会比较简洁,留个坑以后填.
```
def main():
    T = 60 * 60 * 3  # 3小时

    print('run script!')
    tt.__init__()
    t1 = tt.now()
    run_times = 0
    while (tt.during(T)):
        if (tt.stop_0(vk.enter)):  break

        if (tt.get_key_state(vk.back)):
            # back退格键，我的鼠标宏快捷键。建议用T键或者3
            change_position()

        if (tt.get_key_state(vk.symbol[']'])):
            fresh_cd(vk.o)

        temp = tt.now() - t1
        if (temp >= 1):
            # print tt.now() every 5 seconds
            print('--- tt.now():', tt.now(0), '--- run_times:', run_times)
            t1 = tt.now()

        run_times += 1
    
    print('程序已退出, 总运行时间:', tt.now(1), '秒')
```
直接copy源码调试就行.<br>

