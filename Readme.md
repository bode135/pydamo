# pydamo简介

> 对大漠插件的简单封装.

- 提供驱动级按键模拟, 以及修改内存、找图找色等功能.
- 需要管理员权限运行pycharm.<br>
- 仅支持32位python, 最好用`python3.6`
- 基于conda的32位python版本管理
  - 使用`conda`安装`win32`环境脚本: `shells\configWin32Env.bat`.
  - 脚本运行完后会输出创建好的python环境路径, 然后参考[pycharm配置conda安装好的python环境](https://blog.csdn.net/weixin_41710606/article/details/86747877?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_antiscanv2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_antiscanv2&utm_relevant_index=3)
- 64位解决方案参考末尾其它模拟方式



## 更新

- 2024/1/18: 自动admin注册




## 安装

```
shells\configWin32Env.bat       # use conda to create a win32_py36 interpreter

# 推荐通过git clone后, 直接放在代码根目录下使用
pip install -r requirements.txt
```


## 使用

- **第一次使用时必须以管理员权限运行pycharm!**

```
from pydamo import Time, DM, Mouse

dm = DM()   # 可指定dm.dll路径DM(path), 若无法使用某些函数dm.f(), 则使用dm.dm.f()来调用.
ms = Mouse(dm)
tt = Time()

print(ms.position)                  # 当前鼠标位置

tt.sleep(1)
x, y = (0, 0)
ms.position = x, y                  # 移动鼠标
ms.click_right(x, y)                # 点击鼠标右键
```

- More examples:
    - [`test.py`](https://github.com/bode135/pydamo/blob/master/test.py)
    - [`知乎笔记`](https://zhuanlan.zhihu.com/p/266519446 "跳转到知乎")



## 使用条件

1. 32位的python才能运行；
2. 最好使用管理员权限运行（包括pycharm、bat脚本和编译好的exe文件）；
3. 后台绑定挂机为付费的高级功能,我购买的注册码不一定能用很久, 一般用前台键鼠足够。



## 键鼠监听

可用于录制脚本等: ` pynput`, `mouse`, `keyboard`, git搜下照着文档用就行



## 其它模拟方式

> 这些不支持后台键鼠
1. 64位python可以试试Ctypes和keyboard实现驱动级模拟（前台）
    - [`Ctypes`](https://github.com/bode135/VirtualKey_with_Ctypes "跳转到Ctypes")
    - [`keyboard`](https://github.com/boppreh/keyboard "跳转到keyboard项目的git地址")
    - [`mouse`](https://github.com/boppreh/mouse)
    
2. 如果不是D3D游戏的后台模拟的话，可以试试win API的系统级后台模拟SendMessage；

3. 如果键盘为PS/2圆形接口的话，可用winio模块，但不支持USB键盘。

4. python自带方案(最近写原神脚本可以使用的方案)

   2. 基于`ctypes`的可用于原神3D鼠标相对旋转: `pydirectinput.moveRel`(但调用该方案经常被封)
   3. 不是驱动级模拟, 但有时也挺好用: `PyAutoGUI`
   3. `pywin32`直接用` win32api.mouse_event`, 参考[原神钓鱼辅助](https://github.com/IrisRainbowNeko/genshin_auto_fish)



## 打包相关问题

- pyinstaller打包即可, 最好用python3.6环境打包(已知有小伙伴用3.7打包exe出错)

- 也推荐使用embedded-python来打包, windows打包神器, 直接一个独立python, stable-diffusion这些大模型也是用它来免安装python环境直接运行的, 推荐了解下



## 依旧存在的问题

   1. 如何脱离32位python限制? 目前想到的两个方向:
      1. 自己重写一个驱动级dll, 但受限水平(计算机操作系统、驱动编程等相关知识匮乏)而无法实现
      2. 通过Microsoft的文档, 即 `ctypes.windll.user32.SendInput`来实现, 但容易被封
      3. 将pydamo打包为一个后台api服务, 64位程序通过api来调用(目前最可行的方案了)
   2. ~~`pynput`录制的原神脚本都是相对位移, 而`dm.MoveR`和`pydirectinput.moveRel`受限于鼠标加速度(系统加速度或者鼠标自带加速).想要完全复刻必须游戏有没有[仅使用原始输入(Raw Input setting)](https://github.com/learncodebygaming/pydirectinput/issues/57)功能, 不然总会有误差.~~已经用pywin32自带的mouse_event解决3D游戏的相对鼠标位移问题, 重点是去控制面板鼠标速度居中, 并取消windows的"提高鼠标精准度".



