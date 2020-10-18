# 安装
```pip install pydamo-test```<br>
将dm.dll封装成第三方库, 可以当作python包导入直接进行操作.<br>
还在测试阶段所以加上```-test```.
# 使用
**第一次使用时必须以管理员权限运行pycharm!**
```
from pydamo_0 import Time, DM, Mouse, Key, vk
dm = DM()
ms = Mouse(dm)

print(ms.position)                  # 鼠标位置
x, y = (0, 0)
ms.position = x, y                  # 移动鼠标
ms.click_right(x, y)                # 点击鼠标右键
```


# python调用大漠DLL
对大漠插件进行了简单封装，编写了一个简单的[`使用案例`](https://github.com/bode135/pydamo/blob/master/%E7%AE%80%E5%8D%95%E6%A1%88%E4%BE%8B.py)。<br/>
该操作为驱动级模拟,在脚本制作方面强于笔者已知的任何python模块winio,ctypes等。<br/>
附带图色抓取、文字识别、内存读写等接口,详情查阅[`说明文档`](https://github.com/bode135/pydamo/tree/master/%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E)。

# 使用条件:
    1、32位的python才能运行；
    2、最好使用管理员权限运行（包括pycharm、bat脚本和编译好的exe文件）；
    3、后台绑定挂机为付费的高级功能,我购买的注册码不一定能用很久, 一般用前台键鼠足够。

# 其它模拟方式:
    1、64位python可以试试Ctypes实现驱动级模拟（前台）；
    2、如果不是D3D游戏的后台模拟的话，可以试试win API的系统级后台模拟SendMessage；
    3、如果键盘为PS/2圆形接口的话，可用winio模块，但不支持USB键盘。

* 64位python推荐[`Ctypes`](https://github.com/bode135/VirtualKey_with_Ctypes "跳转到Ctypes")。
