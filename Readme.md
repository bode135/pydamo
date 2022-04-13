# pydamo简介

> 对大漠插件的简单封装.

- 提供驱动级按键模拟, 以及修改内存、找图找色等功能.
- 需要管理员权限运行pycharm.<br>
- 仅支持32位python.
- 关于32位python的版本管理, 请看本文最后: 如何用conda管理python, 以及pycharm启用conda创建的win32_python环境
- 64位解决方案: [`基于Ctypes的VirtualKey`](https://github.com/bode135/VirtualKey_with_Ctypes "跳转到 基于Ctypes的VirtualKey"))



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

dm = DM()   # 可指定dm.dll路径DM(path), 若无法使用某些函数dm.f(), 则使用dm.dm.f()来调用.
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

# conda命令

> 使用conda来管理python版本, 参考链接: [csdn-conda安装32位python](https://blog.csdn.net/weixin_41710606/article/details/86747877?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_antiscanv2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_antiscanv2&utm_relevant_index=3)

```
# 一些windows下的重要命令笔记

# 查看操作系统位数
conda info | findstr platform

# 设置为32位
set CONDA_FORCE_32BIT=1

# 创建32位的python3.8
conda create -n win32_py38 python=3.8

# 查看是否成功
conda info -e

# 激活
activate win32_py38

# 查看执行路径
python -c "import sys;print(sys.executable)"

# pycharm启用conda创建的虚拟环境略, 请看上面的参考链接

```
