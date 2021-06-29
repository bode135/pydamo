# pydamo简介
提供驱动级按键模拟, 以及修改内存、找图找色等功能.<br>
需要管理员权限运行pycharm.<br>
仅支持32位python.(64位解决方案: [`基于Ctypes的VirtualKey`](https://github.com/bode135/VirtualKey_with_Ctypes "跳转到 基于Ctypes的VirtualKey"))<br>
对大漠插件的简单封装.<br>
# 安装
```pip install pydamo-test```<br>
---
**2021.1.28日更新:**<br>
> 64位的前台模拟方案推荐: [`keyboard`](https://github.com/boppreh/keyboard "跳转到keyboard项目的git地址").<br>
> 唯一的缺陷就是不支持后台键鼠.<br>
---
# 使用
**第一次使用时必须以管理员权限运行pycharm!**
```
from pydamo_0 import Time, DM, Mouse

dm = DM()
ms = Mouse(dm)
tt = Time()

print(ms.position)                  # 当前鼠标位置

tt.sleep(1)
x, y = (0, 0)
ms.position = x, y                  # 移动鼠标
ms.click_right(x, y)                # 点击鼠标右键
```
更具体使用方式:
[`知乎笔记`](https://zhuanlan.zhihu.com/p/266519446 "跳转到知乎")

# 使用条件:
    1、32位的python才能运行；
    2、最好使用管理员权限运行（包括pycharm、bat脚本和编译好的exe文件）；
    3、后台绑定挂机为付费的高级功能,我购买的注册码不一定能用很久, 一般用前台键鼠足够。

# 其它模拟方式:
    1、64位python可以试试Ctypes实现驱动级模拟（前台）；
    2、如果不是D3D游戏的后台模拟的话，可以试试win API的系统级后台模拟SendMessage；
    3、如果键盘为PS/2圆形接口的话，可用winio模块，但不支持USB键盘。

* 64位python推荐[`Ctypes`](https://github.com/bode135/VirtualKey_with_Ctypes "跳转到Ctypes")。
